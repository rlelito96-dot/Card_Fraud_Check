from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from app.domain.models import Transaction
from app.services.fraud_service import FraudService

from fastapi import Depends
from app.dependencies.fraud_factory import get_fraud_service

from app.domain.models import TransactionStatus

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
async def check_transaction(tx_dto: TransactionDTO, service: FraudService = Depends(get_fraud_service)):
    tx = Transaction(
        id=tx_dto.id,
        user_id=tx_dto.user_id,
        amount=tx_dto.amount,
        country=tx_dto.country,
        timestamp=tx_dto.timestamp,

    )

    result = await service.check_transaction(tx)
    return result