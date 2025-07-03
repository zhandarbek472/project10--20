FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["python", "-m", "app.main"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
