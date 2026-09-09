from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


BASE_DIR = Path(__file__).resolve().parents[2]
STORAGE_DIR = BASE_DIR / "uploads"


def save_upload(file: UploadFile) -> str:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    original_name = Path(file.filename or "uploaded-file").name
    stored_name = f"{uuid4()}_{original_name}"
    destination = STORAGE_DIR / stored_name

    with destination.open("wb") as output_file:
        while chunk := file.file.read(1024 * 1024):
            output_file.write(chunk)

    return str(destination)