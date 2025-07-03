# Python бейнесінен бастаймыз
FROM python:3.12-slim

# Қосымша кодты ішке көшіреміз
WORKDIR /app
COPY . /app

# Тәуелділіктерді орнатамыз
RUN pip install --no-cache-dir -r requirements.txt

# Қосымшаны іске қосамыз
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
