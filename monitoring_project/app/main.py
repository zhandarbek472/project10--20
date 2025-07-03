from fastapi import FastAPI, Request
from app.logging_config import logger
from prometheus_fastapi_instrumentator import Instrumentator
from app.health import router as health_router

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("Request started", extra={
        "method": request.method,
        "url": str(request.url),
    })
    response = await call_next(request)
    logger.info("Request completed", extra={
        "status_code": response.status_code
    })
    return response


# Health Check
app.include_router(health_router)

# Prometheus metrics
Instrumentator().instrument(app).expose(app)
