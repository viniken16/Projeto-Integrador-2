"""Leitura read-only dos marts do PI I para indicadores da landing."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import pandas as pd

from app.config import settings
from app.models import IndicatorKpi, IndicatorsSummary, RendimentoKpi

MART_FILES = (
    "dim_tempo",
    "dim_indicador",
    "dim_recorte",
    "fato_mercado_trabalho",
)


def _read_csv(base: Path, name: str) -> pd.DataFrame:
    path = base / f"{name}.csv"
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def _join_fato(marts: dict[str, pd.DataFrame]) -> pd.DataFrame:
    fato = marts.get("fato_mercado_trabalho", pd.DataFrame())
    if fato.empty:
        return fato

    out = fato.copy()
    for dim_name, keys in [
        ("dim_tempo", ["sk_tempo", "periodo_codigo", "periodo_nome", "ano"]),
        ("dim_indicador", ["sk_indicador", "variavel_nome", "unidade", "categoria_ped"]),
        ("dim_recorte", ["sk_recorte", "eixo", "valor_id", "valor_nome"]),
    ]:
        dim = marts.get(dim_name, pd.DataFrame())
        if dim.empty:
            continue
        merge_key = keys[0]
        if merge_key in out.columns and merge_key in dim.columns:
            cols = [c for c in keys if c in dim.columns]
            out = out.merge(dim[cols], on=merge_key, how="left", suffixes=("", f"_{dim_name}"))
    return out


def _latest_period(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty or "periodo_codigo" not in df.columns:
        return df
    latest = df["periodo_codigo"].astype(str).max()
    return df[df["periodo_codigo"].astype(str) == latest]


def _filter_recorte(df: pd.DataFrame, pattern: str) -> pd.DataFrame:
    if df.empty or "valor_nome" not in df.columns:
        return df
    rx = re.compile(pattern, re.IGNORECASE)
    return df[df["valor_nome"].astype(str).str.contains(rx, na=False)]


def _pick_value(df: pd.DataFrame, tabela: int, recorte_pattern: str | None = None) -> float | None:
    subset = df[df["tabela"] == tabela] if "tabela" in df.columns else df
    if recorte_pattern:
        subset = _filter_recorte(subset, recorte_pattern)
    if subset.empty or "valor" not in subset.columns:
        return None
    try:
        return float(subset.iloc[0]["valor"])
    except (TypeError, ValueError):
        return None


def _informalidade_geral(joined: pd.DataFrame) -> IndicatorKpi:
    rate = _pick_value(joined, 8529)
    if rate is not None and rate > 100:
        rate = rate / 10
    if rate is None:
        rate = 37.3
    return IndicatorKpi(informal=round(rate, 1), formal=round(max(0.0, 100.0 - rate), 1))


def _informalidade_domestica(joined: pd.DataFrame) -> IndicatorKpi:
    subset = joined[joined["tabela"] == 4097] if "tabela" in joined.columns else joined
    if "unidade_medida_nome" in subset.columns:
        subset = subset[subset["unidade_medida_nome"].astype(str).str.contains("Mil pessoas", na=False)]
    domestic = _filter_recorte(subset, r"^Trabalhador dom")
    sem = _pick_value(_filter_recorte(domestic, r"sem carteira"), 4097)
    com = _pick_value(_filter_recorte(domestic, r"com carteira"), 4097)
    if sem is not None and com is not None and (sem + com) > 0:
        pct_sem = sem / (sem + com) * 100
        return IndicatorKpi(informal=round(pct_sem, 1), formal=round(100 - pct_sem, 1))
    return IndicatorKpi(informal=76.2, formal=23.8)


def _rendimento(joined: pd.DataFrame) -> RendimentoKpi:
    subset = joined[joined["tabela"] == 5440] if "tabela" in joined.columns else joined
    domestic = _filter_recorte(subset, r"dom[eé]stic")
    formal = _pick_value(domestic, 5440, r"com carteira")
    informal = _pick_value(domestic, 5440, r"sem carteira")
    if formal is None or informal is None:
        return RendimentoKpi(formal=2251.0, informal=1242.0)
    return RendimentoKpi(formal=round(formal, 2), informal=round(informal, 2))


@lru_cache(maxsize=1)
def load_summary() -> IndicatorsSummary:
    base = Path(settings.marts_dir)
    marts: dict[str, Any] = {name: _read_csv(base, name) for name in MART_FILES}
    joined = _latest_period(_join_fato(marts))
    periodo = None
    if not joined.empty and "periodo_nome" in joined.columns:
        periodo = str(joined["periodo_nome"].dropna().iloc[0])
    fonte = "IBGE PNAD-C / SIDRA (marts do PI I)"
    if not base.exists() or joined.empty:
        fonte = "fallback (marts indisponíveis)"
    return IndicatorsSummary(
        fonte=fonte,
        periodo=periodo,
        informalidade_geral=_informalidade_geral(joined) if not joined.empty else IndicatorKpi(informal=37.3, formal=62.7),
        informalidade_domestica=_informalidade_domestica(joined) if not joined.empty else IndicatorKpi(informal=76.2, formal=23.8),
        rendimento_domestico=_rendimento(joined) if not joined.empty else RendimentoKpi(formal=2251.0, informal=1242.0),
    )
