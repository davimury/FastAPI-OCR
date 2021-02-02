from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import shutil
import ocr
import base64

app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/image", response_class=HTMLResponse)
async def image(request: Request, image: bytes = File(...)):
    base64_image = base64.b64encode(image)
    image_text = ocr.read_image(base64_image)
    return templates.TemplateResponse('image.html', {'request': request, 'image_text': image_text})
