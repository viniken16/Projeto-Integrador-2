"""Configuração da API e caminhos para os marts do PI I."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MARTS = (
    REPO_ROOT
    / "heritage"
    / "pi1"
    / "docs"
    / "Entregaveis"
    / "Unidade3"
    / "projeto_diaristas"
    / "dashboard"
    / "assets"
    / "marts"
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "PI2 Plataforma Diaristas"
    cors_origins: str = "http://localhost:3000"
    marts_dir: Path = DEFAULT_MARTS

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
