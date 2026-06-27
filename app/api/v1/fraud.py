from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies.fraud_factory import get_fraud_service
from app.domain.models import Transaction, TransactionStatus
from app.services.fraud_service import FraudService

router = APIRouter(prefix="/fraud", tags=["fraud"])


class TransactionDTO(BaseModel):
    id: str
    user_id: str
    amount: float
    country: str
    timestamp: datetime


class FraudResponse(BaseModel):
    score: int
    decision: TransactionStatus
    reasons: list[str]


@router.post("/check", response_model=FraudResponse)
async def check_transaction(
    tx_dto: TransactionDTO, service: FraudService = Depends(get_fraud_service)
):
    tx = Transaction(
        id=tx_dto.id,
        user_id=tx_dto.user_id,
        amount=tx_dto.amount,
        country=tx_dto.country,
        timestamp=tx_dto.timestamp,
    )

    result = await service.check_transaction(tx)
    return result
