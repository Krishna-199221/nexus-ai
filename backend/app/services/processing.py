from sqlalchemy.orm import Session

from app.models import Document, DocumentProcessingStatus
from app.services.chunk_persistence import create_document_chunks
from app.services.extraction import extract_text


def process_document(db: Session, document: Document) -> str:
    document.processing_status = DocumentProcessingStatus.PROCESSING
    db.commit()
    db.refresh(document)

    try:
        text = extract_text(
            document.file_path,
            document.document_type,
        )

        create_document_chunks(
            db,
            document,
            text,
        )

        document.processing_status = DocumentProcessingStatus.COMPLETED
        db.commit()
        db.refresh(document)

        return text

    except Exception:
        document.processing_status = DocumentProcessingStatus.FAILED
        db.commit()
        db.refresh(document)

        raise
