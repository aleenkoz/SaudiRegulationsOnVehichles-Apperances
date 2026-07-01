from fastapi import UploadFile, HTTPException
from PIL import Image
import io
import base64

# Allowed image types (could be modified)
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/jpg"}
MAX_SIZE_MB = 10


def validate_and_prepare_image(file: UploadFile):
    # Validate file type
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}. "
                   f"Allowed types: {ALLOWED_TYPES}"
        )

    # Read raw bytes
    raw_bytes = file.file.read()
    file_size_mb = len(raw_bytes) / (1024 * 1024)

    # Validate file size
    if file_size_mb > MAX_SIZE_MB:
        raise HTTPException(
            status_code=400,
            detail=f"File too large: {file_size_mb:.2f} MB. "
                   f"Max allowed is {MAX_SIZE_MB} MB."
        )

    # Validate image integrity
    try:
        Image.open(io.BytesIO(raw_bytes)).verify()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted image file."
        )

    # When everything is validated: Convert to base64 (needed for Ollama vision models)
    encoded = base64.b64encode(raw_bytes).decode("utf-8")

    return {
        "bytes": raw_bytes,
        "base64": encoded,
        "content_type": file.content_type,
        "size_mb": file_size_mb
    }
