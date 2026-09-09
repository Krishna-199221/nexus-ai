from uuid import uuid4

from fastapi.testclient import TestClient

from app.core.database import SessionLocal
from app.main import app
from app.models import Source, User


client = TestClient(app)


def test_create_source():
    db = SessionLocal()

    user = User(
        name="Source API Test User",
        email=f"source-test-{uuid4()}@example.com",
        password_hash="test-password-hash",
        role="developer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    try:
        response = client.post(
            "/api/v1/sources",
            json={
                "name": "Test Resource Report",
                "type": "PDF",
                "location": "uploads/test-resource-report.pdf",
            },
        )

        assert response.status_code == 201

        data = response.json()

        assert data["name"] == "Test Resource Report"
        assert data["type"] == "PDF"
        assert data["location"] == "uploads/test-resource-report.pdf"
        assert data["status"] == "CONNECTED"
        assert data["uploaded_by"] == str(user.id)

        source = db.get(Source, data["id"])

        assert source is not None
        assert source.name == "Test Resource Report"
        assert source.uploaded_by == user.id

    finally:
        source = db.get(Source, data["id"]) if "data" in locals() else None

        if source is not None:
            db.delete(source)

        db.delete(user)
        db.commit()
        db.close()
