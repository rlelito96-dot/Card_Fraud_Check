from typing import Any, Dict

from app.core.config import settings
from app.core.logging import get_logger
from app.domain.engine import FraudEngine
from app.domain.models import Transaction, TransactionStatus

logger = get_logger(__name__)


class FraudService:
    def __init__(self, engine: FraudEngine):
        self.engine = engine

    async def check_transaction(self, tx: Transaction) -> Dict[str, Any]:
        logger.info(
            "Checking transaction",
            extra={
                "tx_id": tx.id,
                "user_id": tx.user_id,
            },
        )

        score, reasons = await self.engine.evaluate(tx)

        decision = self._make_decision(score)

        result = {
            "score": score,
            "decision": decision,
            "reasons": reasons,
        }

        logger.info(
            "Fraud check result",
            extra={
                "tx_id": tx.id,
                "score": score,
                "decision": decision,
            },
        )

        return result

    def _make_decision(self, score: int) -> TransactionStatus:
        if score >= settings.risk_threshold_block:
            return TransactionStatus.BLOCKED

        if score >= settings.risk_threshold_review:
            return TransactionStatus.REVIEW

        return TransactionStatus.APPROVED
