from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from app.domain.models import Transaction
from app.domain.rules import AmountRule, VelocityRule
from app.domain.engine import FraudEngine
from app.infra.redis import RedisClient
from app.infra.repository import FraudRepository
from app.services.fraud_service import FraudService

router = APIRouter(prefix="/fraud", tags=["fraud"])


class TransactionDTO(BaseModel):
    id: str
    user_id: str
    amount: float
    country: str
    timestamp: datetime


redis_client = RedisClient()
repository = FraudRepository(redis_client)
rules = [
    AmountRule(max_amount=1000),
    VelocityRule(repository=repository, max_tx_per_minute=5),

]
engine = FraudEngine(rules)
service = FraudService(engine)

@router.post("/check")
async def check_transaction(tx_dto: TransactionDTO):
    tx = Transaction(
        id=tx_dto.id,
        user_id=tx_dto.user_id,
        amount=tx_dto.amount,
        country=tx_dto.country,
        timestamp=tx_dto.timestamp,

    )

    result = await service.check_transaction(tx)
    return result