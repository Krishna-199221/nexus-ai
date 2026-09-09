from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import Source, User
from app.schemas.source import SourceCreate, SourceResponse

router = APIRouter(
    prefix="/sources",
    tags=["Sources"],
)


def get_development_user_id(db: Session):
    user = db.query(User).first()

    if user is None:
        raise HTTPException(
            status_code=503,
            detail="No development user exists. Authentication setup is required.",
        )

    return user.id


@router.post(
    "",
    response_model=SourceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_source(
    payload: SourceCreate,
    db: Session = Depends(get_db),
):
    user_id = get_development_user_id(db)

    source = Source(
        name=payload.name,
        type=payload.type,
        location=payload.location,
        status="CONNECTED",
        uploaded_by=user_id,
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    return source
