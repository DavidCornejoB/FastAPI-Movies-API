
from pydantic import BaseModel, Field
from typing import Optional
"""
MODELO DE PELÍCULAS:
Se genera un Modelo 'Movie' heredado de BaseModel, para tipar los atributos de 'movie'
"""
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=20)
    overview: str = Field(min_length=20, max_length=200)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    # PARA VALORES POR DEFECTO DE LOS PARÁMETROS
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Título Película",
                "overview": "Descripción Película",
                "year": 2022,
                "rating": 10,
                "category": "Categoría Película",
            }
        }