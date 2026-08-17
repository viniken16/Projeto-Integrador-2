# Herança — Projeto Integrador I

Este diretório preserva a pesquisa, os dados e o dashboard do **PI I**. Eles não são o produto do PI II; são a evidência do problema e a fonte read-only de indicadores.

## O que o PI I entregou

- Exploração do espaço do problema (informalidade no trabalho doméstico / diaristas)
- Pesquisa primária (contratantes e diaristas) e secundária (IBGE PNAD-C / SIDRA, IPEA, SEBRAE)
- Pipeline ETL e modelo dimensional
- Dashboard Streamlit de análise da problemática
- Parceria estratégica com o SEBRAE e ancoragem no ODS 8

Dashboard histórico: [https://pi-trabalho-domestico.streamlit.app](https://pi-trabalho-domestico.streamlit.app)

## Papel dos marts no PI II

Os CSVs versionados em `docs/Entregaveis/Unidade3/projeto_diaristas/dashboard/assets/marts/` alimentam o endpoint `GET /indicators/summary` da API do PI II. A landing do MVP usa esses números para contextualizar confiança, informalidade e rendimento — sem reescrever o Streamlit.

## Como rodar o dashboard antigo

```powershell
cd heritage/pi1/docs/Entregaveis/Unidade3/projeto_diaristas
python -m pip install -r requirements.txt
streamlit run app.py
```

## Estrutura

- `Data/` — planilhas IPEA/IBGE e roteiros/planilhas da pesquisa de campo
- `docs/Entregaveis/` — entregas das cinco unidades do PI I
- `docs/Gerencia de Projeto/` — termo de abertura e EAP do semestre anterior
- `docs/Slides/` — pitches (incluindo SEBRAE)
