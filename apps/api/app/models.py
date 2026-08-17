from datetime import date, datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class UserRole(str, Enum):
    contratante = "contratante"
    diarista = "diarista"


class ServiceRequestStatus(str, Enum):
    pendente = "pendente"
    aceito = "aceito"
    recusado = "recusado"
    concluido = "concluido"
    avaliado = "avaliado"


class User(BaseModel):
    id: str
    email: str
    nome: str
    role: UserRole
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Profile(BaseModel):
    user_id: str
    role: UserRole
    bairro: Optional[str] = None
    cidade: str = "Brasília"
    bio: Optional[str] = None
    verificado: bool = False
    avaliacao_media: Optional[float] = None
    total_avaliacoes: int = 0


class ServiceRequest(BaseModel):
    id: str
    contratante_id: str
    diarista_id: Optional[str] = None
    data_servico: date
    endereco_resumo: str
    status: ServiceRequestStatus = ServiceRequestStatus.pendente
    observacoes: Optional[str] = None


class IndicatorKpi(BaseModel):
    informal: float
    formal: float


class RendimentoKpi(BaseModel):
    formal: float
    informal: float


class IndicatorsSummary(BaseModel):
    fonte: str
    periodo: Optional[str] = None
    informalidade_geral: IndicatorKpi
    informalidade_domestica: IndicatorKpi
    rendimento_domestico: RendimentoKpi
