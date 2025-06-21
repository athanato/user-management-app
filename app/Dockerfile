FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# ✅ Εγκατάσταση εξαρτήσεων και curl
RUN apt-get update && apt-get install -y curl && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "app.py"]
