import pytest
from datetime import datetime

from app.domain.rules import AmountRule
from app.domain.models import Transaction


@pytest.mark.asyncio
async def test_amount_rule_triggers():
    rule = AmountRule(max_amount=1000)

    tx = Transaction(
        id="tx1",
        user_id="user1",
        amount=1500,
        country="PL",
        timestamp=datetime.utcnow()
    )

    result = await rule.apply(tx)

    assert result is not None

    points, reason = result
    assert points == 50
    assert "exceeds limit" in reason

@pytest.mark.asyncio
async def test_amount_rule_not_triggered():
    rule = AmountRule(max_amount=1000)

    tx = Transaction(
        id="tx2",
        user_id="user1",
        amount=500,
        country="PL",
        timestamp=datetime.utcnow()
    )

    result = await rule.apply(tx)

    assert result is None

@pytest.mark.asyncio
async def test_amount_rule_custom_points():
    rule = AmountRule(max_amount=1000, points=80)

    tx = Transaction(
        id="tx3",
        user_id="user1",
        amount=2000,
        country="PL",
        timestamp=datetime.utcnow()
    )

    result = await rule.apply(tx)

    points, _ = result
    assert points == 80
