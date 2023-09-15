from pydantic import BaseModel

"""
MODELO DE USUARIOS:
Se genera un Modelo 'User' heredado de BaseModel. Dentro de éste modelo se tipean los atributos de
correo y contraseña del usuario
"""
class User(BaseModel):
    email: str
    password: str