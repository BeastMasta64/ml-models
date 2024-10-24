FROM python:3.9-slim as builder

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir


FROM python:3.9-slim

WORKDIR /app

COPY  --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

ENV DATABASE_URL 'postgresql://postgres:postgres@db_results:5432/result'

COPY . .

CMD ["bash", "-c", "python rabbitmq.py"]
