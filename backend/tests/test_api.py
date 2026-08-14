from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.schemas import PowerOutageCreate


def test_outage_validation_accepts_valid_data():
    outage = PowerOutageCreate(
        location="Maitumbi",
        state="Niger",
        started_at=datetime(2026, 8, 14, 10, 0),
        restored_at=datetime(2026, 8, 14, 12, 0),
        duration_minutes=120,
        reported_by="Community Reporter",
        description="Power outage reported by a local resident.",
    )

    assert outage.location == "Maitumbi"
    assert outage.state == "Niger"
    assert outage.duration_minutes == 120


def test_outage_validation_rejects_negative_duration():
    with pytest.raises(ValueError):
        PowerOutageCreate(
            location="Maitumbi",
            state="Niger",
            started_at=datetime(2026, 8, 14, 10, 0),
            duration_minutes=-10,
        )


def test_outage_validation_rejects_invalid_restoration_time():
    started_at = datetime(2026, 8, 14, 14, 0)

    with pytest.raises(ValueError):
        PowerOutageCreate(
            location="Maitumbi",
            state="Niger",
            started_at=started_at,
            restored_at=started_at - timedelta(hours=1),
        )


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "NEPA Watch"
    assert data["version"] == "0.1.0"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
