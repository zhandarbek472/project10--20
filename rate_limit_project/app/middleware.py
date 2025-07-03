import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse
import redis.asyncio as redis
import os
from dotenv import load_dotenv

load_dotenv()

RATE_LIMIT = int(os.getenv("RATE_LIMIT", 5))
RATE_PERIOD = int(os.getenv("RATE_PERIOD", 60))
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.redis = redis.Redis.from_url(REDIS_URL, decode_responses=True)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        current = await self.redis.get(key)

        if current is None:
            await self.redis.set(key, 1, ex=RATE_PERIOD)
        elif int(current) < RATE_LIMIT:
            await self.redis.incr(key)
        else:
            retry_after = await self.redis.ttl(key)
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests", "retry_after": retry_after}
            )

        response = await call_next(request)
        return response
