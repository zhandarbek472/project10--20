from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CI/CD және Deploy сәтті жұмыс істейді!"}
