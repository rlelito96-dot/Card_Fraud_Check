import pytest
from datetime import datetime

from app.domain.engine import FraudEngine
from app.domain.models import Transaction
from app.domain.rules import AmountRule

@pytest.mark.asyncio
async def test_engine_amount_rule_triggers():
    engine = FraudEngine(
        rules=[AmountRule(max_amount=1000)]
    )

    tx = Transaction(
        id="tx1",
        user_id="user1",
        amount=1500,
        country ="PL",
        timestamp =datetime.utcnow()

    )

    score, reasons = await engine.evaluate(tx)

    assert score == 50
    assert len(reasons) == 1
    assert "exceeds limit" in reasons[0]