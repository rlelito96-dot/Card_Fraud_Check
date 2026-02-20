# 💳 Card Fraud Check Service

## Project Description

An **asynchronous service for detecting potential credit card fraud**.  
This project demonstrates **clean architecture**, a **domain layer**, **Redis-based velocity rules**, and **unit and integration testing**.  

**Features:**

- Evaluate transactions using configurable fraud rules  
- Risk assessment with decisions: `APPROVE`, `REVIEW`, `BLOCK`  
- Example rules: `AmountRule`, `VelocityRule` (using Redis)  
- Modular engine and service for easy rule expansion  
- Unit tests (`rules`, `engine`) and integration tests (`FastAPI endpoint`)  
- Asynchronous operations and Redis integration  
- Docker + docker-compose for local development and testing  

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

## Installation / Setup

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd Card_Fraud_Check_Project


## Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows PowerShell

## Install dependencies
pip install -r requirements.txt

## Environment Variables
REDIS_URL=redis://redis:6379
RISK_THRESHOLD_BLOCK=70
RISK_THRESHOLD_REVIEW=40

## Running the Server
docker-compose up
### or locally
uvicorn app.main:app --reload

### Default FastAPI URL: http://localhost:8000
### Endpoint: POST /api/v1/fraud/check

## Tests
pytest -v

## Docker
docker-compose up -d
docker-compose logs -f api

### Ports: 
FastAPI: 8000
Redis: 6379

## CI/CD
Prepared for GitHub Actions:

Automatic tests on push/pull requests

Optional linting: flake8, black, isort

Docker build verification