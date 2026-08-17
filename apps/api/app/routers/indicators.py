from fastapi import APIRouter

from app.models import IndicatorsSummary
from app.services.marts import load_summary

router = APIRouter(prefix="/indicators", tags=["indicators"])


@router.get("/summary", response_model=IndicatorsSummary)
def indicators_summary() -> IndicatorsSummary:
    return load_summary()
