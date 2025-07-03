from fastapi import FastAPI
from app.middleware import RateLimiterMiddleware

app = FastAPI()

# Middleware-ді тіркеу
app.add_middleware(RateLimiterMiddleware)

@app.get("/")
async def root():
    return {"message": "Бәрі жақсы, бұл шектелмеген сұраныс!"}

@app.get("/ping")
async def ping():
    return {"message": "Pong!"}
