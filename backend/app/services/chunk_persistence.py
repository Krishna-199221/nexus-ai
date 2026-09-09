from sqlalchemy.orm import Session

from app.models import Document, DocumentChunk
from app.services.chunking import chunk_text


def create_document_chunks(
    db: Session,
    document: Document,
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[DocumentChunk]:
    """
    Create and persist chunks for a document.

    Existing chunks for the document are removed first so that
    reprocessing the same document does not create duplicates.
    """

    chunks = chunk_text(
        text,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    existing_chunks = (
        db.query(DocumentChunk)
        .filter(DocumentChunk.document_id == document.id)
        .all()
    )

    for existing_chunk in existing_chunks:
        db.delete(existing_chunk)

    db.flush()

    document_chunks = []

    for index, content in enumerate(chunks):
        document_chunk = DocumentChunk(
            document_id=document.id,
            content=content,
            chunk_index=index,
        )

        db.add(document_chunk)
        document_chunks.append(document_chunk)

    db.commit()

    for document_chunk in document_chunks:
        db.refresh(document_chunk)

    return document_chunks
