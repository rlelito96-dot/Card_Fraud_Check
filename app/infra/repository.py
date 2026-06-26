from app.infra.redis import RedisClient
from app.core.logging import get_logger

logger = get_logger(__name__)

class FraudRepository:
    def __init__(self, redis_client: RedisClient):
        self.redis_client = redis_client

    async def incr_user_tx(self, user_id: str, expire_seconds: int = 60) -> int:
        client = await self.redis_client.connect()
        key = f"user:{user_id}:tx"
        count = await client.incr(key)
        await client.expire(key, expire_seconds)

        logger.debug(f"Incremented transaction count for {user_id}: {count}")
        return count

    async def get_user_tx_count(self, user_id: str) -> int:
        client = await self.redis_client.connect()
        key = f"user:{user_id}:tx"
        count = await client.get(key)
        return int(count) if count else 0