from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import os

app = FastAPI()

# Diretório de templates HTML
templates = Jinja2Templates(directory="templates")

# Rota principal: exibe a interface web
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para listar avatares da Heygen
@app.get("/api/avatars")
def get_avatars():
    headers = {
        "Authorization": f"Bearer {os.getenv('HEYGEN_API_KEY')}"
    }
    response = requests.get("https://api.heygen.com/v2/avatars", headers=headers)
    return JSONResponse(content=response.json())

# Rota para listar vozes da Heygen
@app.get("/api/voices")
def get_voices():
    headers = {
        "Authorization": f"Bearer {os.getenv('HEYGEN_API_KEY')}"
    }
    response = requests.get("https://api.heygen.com/v2/voices", headers=headers)
    return JSONResponse(content=response.json())
