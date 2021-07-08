# FastAPI con modelos relacionales en MySQL
![imagen](https://user-images.githubusercontent.com/37969577/124988090-2ed27400-e003-11eb-9363-132acdd2b871.png)

API para registro de usuarios con FastAPI, SQLAlchemy y MySQL.
El modelo planteado es una relaclión uno a uno entre una persona y un usuario. Todos los Endpoint están documentados utilizando Swagger.

Cada API tiene su respectivo modelo de entrada y respuesta, utilizando Pydantic que está soportado nativamente por FastAPI.

## Pasos para configuración

**1. Clona la aplicación**

```bash
git clone https://github.com/pjavier1988/fastapi-mysqlFK.git
```

**2. Crea una base de datos Mysql**
```bash
create database fastapi_relationship
```

**3. Modifica los datos de configuración**

+ abre el archivo `app/settings.py`
+ modifica `database_url` de acuerdo a la configuración de tu base de datos
```bash
mysql+mysqlconnector://root:12345@127.0.0.1:3306/fastapi_relationship
```
+ adicionalmente, puedes modificar el host y el puerto del servidor.
 
**4. Configura el ambiente**
+ configura un ambiente virtual, con una versión de Python 3.x.x (en Linux)
```bash
virtualenv env -p python3
```
+ activa el ambiente virtual (en Linux)
```bash
source env/bin/activate 
```
+ instala las dependencias
```bash
pip install -r requirements.txt
```
**4. Ejecuta**
Para lanzar el aplicativo, debes ubicarte en el directorio app y ejecutar el comando

```bash
uvicorn asgi:app --reload
```
La aplicación se ejecutará en <http://127.0.0.1:8000>

## Rest APIs

La app define algunos servicios de CRUD APIs.

### Person

| Method | Url | Decription |
| ------ | --- | ---------- | 
| GET   | /person/list-persons | Listar personas |  
| POST   | /person/persons | Crear personas | 

### Users

| Método | Url | Descripción | 
| ------ | --- | ----------- | 
| GET    | /user/list-users | Lista los usuarios | 
| POST    | /user/register | Permite el registro de un usuario |

