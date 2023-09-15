from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder

# MIDDLEWARE PARA AUTENTICACIÓN DE USUARIOS:
from middlewares.jwt_bearer import JWTBearer

# CONEXIÓN CON BASE DE DATOS SQLITE:
from config.database import Session

# IMPORTAMOS MODELO CREADO
from models.movie import Movie as MovieModel

# PARA ROUTER
from fastapi import APIRouter

# PARA SERVICIOS
from services.movie import MovieService

# PARA ESQUEMAS
from schemas.movie import Movie

movie_router = APIRouter()

""" 
OBTENER LA LISTA DE PELÍCULAS:
Endpoint que retorna toda la lista de películas sin ningún filtro.
"""
@movie_router.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    try:
        db = Session()
        result = MovieService(db).get_movies()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except:
        return JSONResponse(status_code=400, content={"message": "Error. Bad Request"})

"""
OBTENER UNA PELÍCULA POR SU ID:
Endpoint que recibe una id como parámetro de ruta, y retorna la película que posea ésa id.
Si no existe una película con ésa id, retorna un mensaje de error con el código de estado 404.
"""
@movie_router.get("/movies/{id}", tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movie(id: int = Path(ge=1)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encuentra una película con ésa id"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

"""
OBTENER UNA PELÍCULA POR SU CATEGORÍA (QUERY PARAM):
Endpoint que recibe un str de categoría como Query Param y retorna la película que posea dicha categoría.
En caso de no haber una película con ésa categoría, retorna un mensaje con código de estado 404.

"""
@movie_router.get("/movies/", tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404,content={"message": "No se encuentra una película que pertenezca a ésa categoría"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

"""
INSERTAR UNA PELÍCULA:
Endpoint que recibe un diccionario de tipo 'Movie' y lo añade a la lista de películas
"""
@movie_router.post("/movies", tags=["movies"], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_movie(movie: Movie) -> dict:
    try:
        db = Session()
        MovieService(db).create_movie(movie)
        return JSONResponse(status_code=201, content={"message": "Se ha registrado la película en la Base de Datos"})
    except:
        return JSONResponse(status_code=422, content={"message": "Error al insertar la película"})

"""
ACTUALIZAR UNA PELÍCULA POR SU ID:
Endpoint que recibe una id como parámetro de ruta, y un diccionario de película con los datos a actualizarse.
Primero se hace una búsqueda de una pelicula con dicha id, y una vez encontrada, se modifican sus valores.
"""
@movie_router.put("/movies/{id}", tags=["movies"], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Error. No se encontró una película con ésa id."})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=201, content={"message": "Película modificada con éxito"})

"""
ELIMINAR UNA PELÍCULA POR SU ID:
Endpoint que recibe una id como parámetro de ruta, hace una búsqueda de una película con dicha id y la elimina
de la lista de películas.
"""
@movie_router.delete("/movies/{id}", tags=["movies"], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Error. No se encontró una película con ésa id."})
    MovieService(db).delete_movie(result)
    return JSONResponse(status_code=200, content={"message": "Película eliminada con éxito"})