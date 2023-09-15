import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
CREAR UNA DIRECCIÓN URL DE LA BASE DE DATOS PARA SQLALCHEMY:
Nos estamos conectando a una base de datos SQLite (abriendo un archivo con la base de datos SQLite)
"""
sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

"""
CREAR UN "MOTOR" SQLALCHEMY
"""
engine = create_engine(database_url, echo=True)

"""
CREAR UNA CLASE SESSION:
Cada instancia de la clase será una sesión de base de datos. La clase en sí aúbn no es una sesión de base de datos.
Pero, una vez que creamos una instancia de la clase, ésta instancia será la sesión de la base de datos local.
"""
Session = sessionmaker(bind=engine)

"""
CREAR UNA CLASE BASE:
Usamos la función que devuelve una clase .declarative_base()
Posteriormente, heredamos de ésta clase para crear cada uno de los modelos o clases de la base de datos (modelos ORM)
"""
Base = declarative_base()