import redis.asyncio as redis
from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

class RedisClient:
    def __init__(self, url: str | None = None):
        self.url = url or settings.redis_url
        self._client: redis.Redis | None = None

    async def connect(self) -> redis.Redis:
        if self._client is None:
            logger.info("Connecting to Redis", extra={"url": self.url})
            self._client = redis.from_url(
                self.url,
                decode_response=True,
            )
        return self._client

    async def close(self) -> None:
        if self._client:
            logger.info("Closing Redis connection")
            await self._client.close()
            self._client = None