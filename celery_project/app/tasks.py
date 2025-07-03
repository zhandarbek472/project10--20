from celery import Celery
import time

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def send_email(to: str):
    print(f"Отправка письма на {to} началась...")
    time.sleep(5)
    print(f"Письмо отправлено на {to}")
    return {"status": "sent", "to": to}
