from io import BytesIO
from uuid import uuid4

from fastapi.testclient import TestClient

from app.core.database import SessionLocal
from app.main import app
from app.models import Document, Source, User


client = TestClient(app)


def test_upload_document():
    db = SessionLocal()

    user = User(
        name="Document API Test User",
        email=f"document-test-{uuid4()}@example.com",
        password_hash="test-password-hash",
        role="developer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    source = Source(
        name="Document Upload Test Source",
        type="LOCAL",
        location="test",
        status="CONNECTED",
        uploaded_by=user.id,
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    stored_path = None

    try:
        response = client.post(
            f"/api/v1/sources/{source.id}/documents",
            files={
                "file": (
                    "test-document.txt",
                    BytesIO(b"NEXUS AI document ingestion test"),
                    "text/plain",
                )
            },
        )

        assert response.status_code == 201

        data = response.json()

        assert data["source_id"] == str(source.id)
        assert data["filename"] == "test-document.txt"
        assert data["document_type"] == "TXT"
        assert data["processing_status"] == "COMPLETED"

        document = db.get(Document, data["id"])

        assert document is not None
        assert document.source_id == source.id
        assert document.filename == "test-document.txt"
        assert document.processing_status.value == "COMPLETED"

        stored_path = document.file_path

    finally:
        document = None

        if stored_path:
            document = db.get(Document, data["id"])

        if document is not None:
            db.delete(document)

        db.delete(source)
        db.delete(user)
        db.commit()
        db.close()

    if stored_path:
        from pathlib import Path

        Path(stored_path).unlink(missing_ok=True)


def test_upload_document_source_not_found():
    source_id = uuid4()

    response = client.post(
        f"/api/v1/sources/{source_id}/documents",
        files={
            "file": (
                "test-document.txt",
                BytesIO(b"test"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Source not found"


def test_upload_document_unsupported_file_type():
    db = SessionLocal()

    user = User(
        name="Unsupported File Test User",
        email=f"unsupported-test-{uuid4()}@example.com",
        password_hash="test-password-hash",
        role="developer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    source = Source(
        name="Unsupported File Test Source",
        type="LOCAL",
        location="test",
        status="CONNECTED",
        uploaded_by=user.id,
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    try:
        response = client.post(
            f"/api/v1/sources/{source.id}/documents",
            files={
                "file": (
                    "malware.exe",
                    BytesIO(b"not really malware"),
                    "application/octet-stream",
                )
            },
        )

        assert response.status_code == 400
        assert response.json()["detail"] == "Unsupported file type"

    finally:
        db.delete(source)
        db.delete(user)
        db.commit()
        db.close()
