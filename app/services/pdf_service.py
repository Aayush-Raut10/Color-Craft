from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from PIL import Image


def images_to_pdf(images, pdf_path):

    c = canvas.Canvas(str(pdf_path), pagesize=A4)

    width, height = A4

    for image_path in images:

        img = Image.open(image_path)

        img_width, img_height = img.size

        ratio = min(width / img_width, height / img_height)

        w = img_width * ratio

        h = img_height * ratio

        x = (width - w) / 2

        y = (height - h) / 2

        c.drawImage(str(image_path), x, y, width=w, height=h)

        c.showPage()

    c.save()