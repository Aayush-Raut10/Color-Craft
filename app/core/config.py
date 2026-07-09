import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "ColorCraft AI"
    HF_API_TOKEN:str = os.getenv("HF_API_TOKEN")

settings = Settings()