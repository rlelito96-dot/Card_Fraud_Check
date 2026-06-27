# 💳 Card Fraud Check Service

Asynchronous fraud detection service using FastAPI, Redis and rule-based engine.

---

## 🚀 Quick Start

```bash
cp .env.example .env
docker compose up -d
docker compose run api pytest
```

---

## 📦 Full Setup

### 1. Clone repository

```bash
git clone https://github.com/rlelito96-dot/Card_Fraud_Check.git
cd Card_Fraud_Check
```

### 2. Create environment file

```bash
cp .env.example .env
```

### 3. Start database (Docker)

```bash
docker compose up -d
```

---

## 🧠 Features
- Fraud scoring engine (rule-based)
- Transaction evaluation:
  - AmountRule (high value detection)
  - VelocityRule (Redis-based frequency detection)
- Decisions:
  - APPROVED
  - REVIEW
  - BLOCKED
- Async architecture (FastAPI + async Redis)
- Clean architecture (domain / service / infra separation)
- Fully containerized environment

---

## 📦 Architecture

Service is fully containerized:

- API → FastAPI (Python 3.12)
- Redis → used for velocity rules
- Tests → executed inside API container
- No local Python required

---

## Technologies

- Python 3.12+  
- FastAPI  
- Redis  
- Pydantic / dataclasses  
- Pytest / pytest-asyncio  
- Docker / docker-compose  
- GitHub Actions CI/CD  

---

# 🧪 Tests

```bash
docker compose run api pytest
```

---

# 📖 API Documentation

- *API*: http://localhost:8000
- *Swagger docs*: http://localhost:8000/docs
- *Redoc*: http://localhost:8000/redoc

---

## 🔄 CI/CD Ready

Project is prepared for CI pipelines:

- tests run in isolated container
- Redis provided via docker-compose
- no local dependencies required

## ❗ Important Notes
- Do NOT run pytest locally
- Do NOT install dependencies manually on host
- Everything runs inside Docker containers