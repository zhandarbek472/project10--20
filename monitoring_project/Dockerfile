# Базалық бейне
FROM python:3.12-slim

# Жұмыс директория
WORKDIR /app

# Тәуелділіктерді көшіру және орнату
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Қолданба кодын көшіру
COPY . .

# Uvicorn арқылы іске қосу
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
