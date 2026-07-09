from pydantic import BaseModel, Field, field_validator

class ColoringBookRequest(BaseModel):
    theme: str = Field(..., min_length=1, max_length=100)
    pages: int = Field(..., ge=1, le=15)
    age:int = Field(..., ge=2, le=10)

    @field_validator("theme")
    @classmethod
    def strip_and_validate_theme(cls, v: str) -> str:
        cleaned = v.strip()
        if not cleaned:
            raise ValueError("Theme cannot be blank.")
        return cleaned