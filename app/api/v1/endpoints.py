from pathlib import Path
import uuid
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import FileResponse
from app.schemas.coloring_book import ColoringBookRequest
from app.services.gemini_service import generate_page
from app.services.pdf_service import images_to_pdf


router = APIRouter(prefix="/api/v1", tags=["Coloring Books"])

IMAGE_DIR = Path("output/images")
PDF_DIR = Path("output/pdf")

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
PDF_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/colorbook", status_code=status.HTTP_200_OK)
def generate_coloring_book(request: ColoringBookRequest) -> FileResponse:

    images = []

    folder = IMAGE_DIR / str(uuid.uuid4())

    folder.mkdir()

    try:
        for page in range(request.pages):

            image = generate_page(
                theme=request.theme,
                age=request.age,
                page_number=page + 1,
                output_dir=folder,
            )

            images.append(image)
    except Exception:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="You have reached the free 1-month limit."
)
    
    pdf_path = PDF_DIR / f"{uuid.uuid4()}.pdf"

    images_to_pdf(images, pdf_path)

    return FileResponse(
        path=pdf_path,
        filename="coloring_book.pdf",
        media_type="application/pdf",
    )