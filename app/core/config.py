import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "ColorCraft AI"
    HF_API_TOKEN:str = os.getenv("HF_API_TOKEN")
    
    MAX_CONCURRENT_IMAGE_GENERATIONS: int = 10
    GEMINI_MAX_RETRIES: int = 10
    GEMINI_RETRY_BACKOFF_FACTOR: float = 2.0
    
    ENV: str = "production"

settings = Settings()