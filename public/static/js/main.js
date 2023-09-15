let descripcion = document.getElementById("textoDescripcion");

descripcion.innerHTML = 
`
La siguiente aplicación ha sido desarrollada en FastAPI, y consta de un CRUD de películas. 

Todos los registros están siendo almacenados en una base de datos de SQLite. 
Cada uno de los endpoints requieren de autentificación de usuario, por lo que primero se deberá acceder al endpoint de
'user' y loguearse con las siguientes credenciales:
`;
