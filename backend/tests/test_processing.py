from pathlib import Path
from uuid import uuid4

import pytest

from app.core.database import SessionLocal
from app.models import (
    Document,
    DocumentProcessingStatus,
    Source,
    User,
)
from app.services.processing import process_document


def test_process_document_success(tmp_path: Path):
    db = SessionLocal()

    user = User(
        name="Processing Test User",
        email=f"processing-test-{uuid4()}@example.com",
        password_hash="test-password-hash",
        role="developer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    source = Source(
        name="Processing Test Source",
        type="LOCAL",
        location="test",
        status="CONNECTED",
        uploaded_by=user.id,
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "NEXUS AI processing test",
        encoding="utf-8",
    )

    document = Document(
        source_id=source.id,
        filename="sample.txt",
        document_type="TXT",
        file_path=str(file_path),
        processing_status=DocumentProcessingStatus.UPLOADED,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    try:
        result = process_document(db, document)

        assert result == "NEXUS AI processing test"
        assert (
            document.processing_status
            == DocumentProcessingStatus.COMPLETED
        )

    finally:
        db.delete(document)
        db.delete(source)
        db.delete(user)
        db.commit()
        db.close()


def test_process_document_failure(tmp_path: Path):
    db = SessionLocal()

    user = User(
        name="Processing Failure Test User",
        email=f"processing-failure-{uuid4()}@example.com",
        password_hash="test-password-hash",
        role="developer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    source = Source(
        name="Processing Failure Test Source",
        type="LOCAL",
        location="test",
        status="CONNECTED",
        uploaded_by=user.id,
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    file_path = tmp_path / "missing.txt"

    document = Document(
        source_id=source.id,
        filename="missing.txt",
        document_type="TXT",
        file_path=str(file_path),
        processing_status=DocumentProcessingStatus.UPLOADED,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    try:
        with pytest.raises(FileNotFoundError):
            process_document(db, document)

        assert (
            document.processing_status
            == DocumentProcessingStatus.FAILED
        )

    finally:
        db.delete(document)
        db.delete(source)
        db.delete(user)
        db.commit()
        db.close()
