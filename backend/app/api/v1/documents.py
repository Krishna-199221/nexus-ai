from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import Document, DocumentProcessingStatus, Source
from app.schemas.document import DocumentResponse
from app.services.storage import save_upload


router = APIRouter(
    prefix="/sources/{source_id}/documents",
    tags=["Documents"],
)


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".csv",
    ".xlsx",
}


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=201,
)
def upload_document(
    source_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    source = db.get(Source, source_id)

    if source is None:
        raise HTTPException(
            status_code=404,
            detail="Source not found",
        )

    filename = Path(file.filename or "").name

    if not filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required",
        )

    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type",
        )

    stored_path = save_upload(file)

    document = Document(
        source_id=source.id,
        filename=filename,
        document_type=extension.lstrip(".").upper(),
        file_path=stored_path,
        processing_status=DocumentProcessingStatus.UPLOADED,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document
