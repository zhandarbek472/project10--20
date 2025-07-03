from fastapi import FastAPI
from app.tasks import send_email

app = FastAPI()

@app.post("/send-email/")
def trigger_email(to: str):
    send_email.delay(to)
    return {"message": f"Письмо отправляется на {to}..."}
