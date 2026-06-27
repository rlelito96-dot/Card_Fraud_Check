from typing import List, Optional, Tuple

from app.domain.models import Transaction
from app.domain.rules import FraudRule


class FraudEngine:
    """Transaction evaluation engine"""

    def __init__(self, rules: List[FraudRule]):
        self.rules = rules

    async def evaluate(self, tx: Transaction) -> Tuple[int, List[str]]:
        """Evaluation of a single transaction"""
        score = 0
        reasons: List[str] = []

        for rule in self.rules:
            result: Optional[Tuple[int, str]] = await rule.apply(tx)
            if result:
                points, reason = result
                score += points
                reasons.append(reason)

        return score, reasons
