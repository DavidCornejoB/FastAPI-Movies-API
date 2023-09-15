from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from utils.jwt_manager import validate_token

"""
CLASE JWTBEARER:
Posee una función asíncrona que recibe una petición con el token generado al iniciar sesión.
Se envía dicho token a la función 'validate_token()' para validarla y poder usar los Endpoints.
"""
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales inválidas")