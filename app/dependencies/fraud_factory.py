from app.domain.engine import FraudEngine
from app.domain.rules import AmountRule, VelocityRule
from app.infra.redis import RedisClient
from app.infra.repository import FraudRepository
from app.services.fraud_service import FraudService


def get_fraud_service():
    redis_client = RedisClient()
    repository = FraudRepository(redis_client)

    rules = [
        AmountRule(max_amount=1000),
        VelocityRule(repository=repository, max_tx_per_minute=5),
    ]

    engine = FraudEngine(rules)
    return FraudService(engine)
