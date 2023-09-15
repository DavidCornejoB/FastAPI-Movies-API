from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

# ROUTER:
from routers.movie import movie_router
from routers.user import user_router

# MIDDLEWARE PARA MANEJO DE ERRORES:
from middlewares.error_handler import ErrorHandler

# TOKEN:
from utils.jwt_manager import create_token

# CONEXIÓN CON BASE DE DATOS SQLITE:
from config.database import engine, Base

# INFORMACIÓN DE LA APP:
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.description = "Aplicación de creación de API REST para un CRUD de películas con autenticación de usuario y generación de tokens"
app.version = "0.2.0"
app.contact = {
        "name": "David Cornejo B",
        "url": "https://github.com/DavidCornejoB/FastAPI-Movies-API",
        "email": "luisdavidcorbra24@gmail.com"
    }

# LLAMADA A MIDDLEWARE PARA CONTROL DE ERRORES EN LA APP
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

# MANEJO DE ARCHIVOS ESTÁTICOS (CSS, JS)
app.mount("/static", StaticFiles(directory="./public/static"), name="static")

# CREACIÓN DE TODAS LAS TABLAS DE LA BASE DE DATOS:
Base.metadata.create_all(bind=engine)

"""
ENDPOINT PARA HOME
"""
@app.get("/", tags=["home"], response_class=FileResponse)
def message():
    html_address = './public/static/index.html'
    return FileResponse(html_address, status_code=200)