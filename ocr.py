import pytesseract as ocr
from PIL import Image
import base64
import io

ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_image(image):
    image_string = io.BytesIO(base64.b64decode(image))
    final_image = Image.open(image_string)
    phrase = ocr.image_to_string(final_image, lang='por')
    return phrase
