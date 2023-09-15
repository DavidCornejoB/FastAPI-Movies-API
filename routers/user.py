from fastapi.responses import JSONResponse

# TOKEN:
from utils.jwt_manager import create_token

# PARA ROUTER
from fastapi import APIRouter

# PARA ESQUEMA
from schemas.user import User

user_router = APIRouter()

"""
LOGIN DE USUARIOS:
Endpoint que recibe el email y contraseña del usuario y los valida para generar o no un token para poder
utilizar el resto de endpoints.
"""
@user_router.post("/login", tags=["auth"], response_model=str, status_code=200)
def login(user: User) -> str:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=401, content={"message": "Credenciales inválidas, intente nuevamente"})