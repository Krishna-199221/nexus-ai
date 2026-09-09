from pathlib import Path
from uuid import uuid4

from app.core.database import SessionLocal
from app.models import Document, DocumentChunk, Source, User
from app.services.chunk_persistence import create_document_chunks


def test_create_document_chunks(tmp_path: Path):
    db = SessionLocal()

    user = User(
        name="Chunk Persistence Test User",
        email=f"chunk-persistence-{uuid4()}@example.com",
        password_hash="test-password-hash",
        role="developer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    source = Source(
        name="Chunk Persistence Test Source",
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
        "NEXUS AI chunk persistence test",
        encoding="utf-8",
    )

    document = Document(
        source_id=source.id,
        filename="sample.txt",
        document_type="TXT",
        file_path=str(file_path),
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    try:
        result = create_document_chunks(
            db,
            document,
            "ABCDEFGHIJ" * 3,
            chunk_size=10,
            chunk_overlap=2,
        )

        assert len(result) == 4

        assert result[0].content == "ABCDEFGHIJ"
        assert result[0].chunk_index == 0

        assert result[1].content == "IJABCDEFGH"
        assert result[1].chunk_index == 1

        assert result[2].content == "GHIJABCDEF"
        assert result[2].chunk_index == 2

        assert result[3].content == "EFGHIJ"
        assert result[3].chunk_index == 3

        stored_chunks = (
            db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document.id)
            .order_by(DocumentChunk.chunk_index)
            .all()
        )

        assert len(stored_chunks) == 4
        assert all(
            chunk.document_id == document.id
            for chunk in stored_chunks
        )

    finally:
        db.delete(document)
        db.delete(source)
        db.delete(user)
        db.commit()
        db.close()
