from abc import ABC, abstractmethod
from typing import Optional, Tuple
from app.domain.models import Transaction
from app.infra.repository import FraudRepository

class FraudRule(ABC):
    @abstractmethod
    async def apply(self, tx: Transaction) -> Optional[Tuple[int, str]]:
        """Transaction evaluation"""
        pass

class AmountRule(FraudRule):
    def __init__(self, max_amount: float, points: int = 50):
        self.max_amount = max_amount
        self.points = points

    async def apply(self, tx: Transaction) -> Optional[Tuple[int, str]]:
        if tx.amount > self.max_amount:
            return self.points, f"Transaction amount {tx.amount} exceeds limit {self.max_amount}"
        return None

class VelocityRule(FraudRule):
    def __init__(self, repository: FraudRepository, max_tx_per_minute: int = 5, points: int = 30):
        self.repository = repository
        self.max_tx = max_tx_per_minute
        self.points = points

    async def apply(self, tx: Transaction) -> Optional[Tuple[int, str]]:
        try:
            count = await self.repository.incr_user_tx(tx.user_id, expire_seconds=60)

            if count > self.max_tx:
                return self.points, (
                    f"High transaction velocity: {count} "
                    f"transactions in last minute"
                )

            return None

        except Exception:
            # fail-safe: rule nie może wywalić całego engine
            return 0, "velocity rule failed (redis error)"