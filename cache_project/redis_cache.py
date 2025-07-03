import redis.asyncio as redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

async def get_cache(key: str):
    data = await redis_client.get(key)
    if data:
        return json.loads(data)
    return None

async def set_cache(key: str, value, expire_seconds: int = 60):
    await redis_client.set(key, json.dumps(value), ex=expire_seconds)

async def delete_cache(key: str):
    await redis_client.delete(key)
