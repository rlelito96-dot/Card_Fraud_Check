from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_fraud_check():
    payload = {
        "id": "tx1",
        "user_id": "user1",
        "amount": 1500,
        "country": "PL",
        "timestamp": datetime.utcnow().isoformat(),
    }

    response = client.post("/api/v1/fraud/check", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "score" in data
    assert "decision" in data
    assert isinstance(data["reasons"], list)
