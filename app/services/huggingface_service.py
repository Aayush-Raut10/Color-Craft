from pathlib import Path
from app.core.config import settings
from huggingface_hub import InferenceClient

client = InferenceClient(token=settings.HF_API_TOKEN)



def generate_page(theme: str, age: int, page_number: int, output_dir: Path):

    prompt = f"""
            Create a printable children's coloring page.

            Theme: {theme}

            Child age: {age}

            Requirements:

            - Black and white
            - Thick outlines
            - No shading
            - No grayscale
            - White background
            - One large main object
            - Simple details
            - Portrait
            - Coloring book style
            - High quality
            - Different composition from previous pages

            Note: Different images from previous pages
            """
    
    image = client.text_to_image(
        prompt,
        model = "stabilityai/stable-diffusion-2-1"  # model="black-forest-labs/FLUX.1-schnell"
    )

    output_path = output_dir / f"page_{page_number}.png"

    image.save(output_path)

    return output_path
    