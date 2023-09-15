# Aplicación de CRUD de películas con FastAPI

## Qué es FastAPI?
Es un framework moderno de alto rendimiento para creación de APIs con Python
* Rápido
* Menor tendencia a errores
* Fácil e intuitivo
* Robusto
* Basada en estándares: OpenAPI

---

## Instalación de FastAPI:
Versión de Python utilizada: 3.7.9

1. Creamos un entorno de Python en donde se ejecutará el servidor web **Uvicorn**
```
python -m venv mi-entorno
```
2. Activamos el entorno creado:
```
mi-entorno/Scripts/activate
```
3. Antes de la instalación de FastAPI y Uvicorn, realizamos un upgrade de pip:
```
python.exe -m pip install --upgrade pip
```
4. Instalación de FastAPI y Uvicorn
```
pip install fastapi
```
```
pip install uvicorn
```

---

## Ejecución de la aplicación:
Suponiendo que todo el código lo tenemos en un archivo ```main.py```, para correr la aplicación ejecutamos:
```
uvicorn main:app
```
Para que los cambios realizados en el código de la aplicación corran automáticamente:
```
uvicorn main:app --reload
```
Correr la aplicación en un puerto específico:
```
uvicorn main:app --port 5000
```
Exteriorizar la aplicación dentro de la red, para poder acceder a dicha aplicación desde otros dispositivos dentro de la red:
```
uvicorn main:app --host 0.0.0.0
```

---

## Documentación automática con Swagger:
FastAPI integra documentación con Swagger. Para acceder a dicha documentación, corremos la aplicación y accedemos al siguiente enlace:
```
http://127.0.0.1:8000/docs
```
