from fastapi import FastAPI
from app.config import settings
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "host": settings.app_host,
        "port": settings.app_port
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.app_host, port=settings.app_port)

