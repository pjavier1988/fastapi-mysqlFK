from fastapi import FastAPI

from api import router

tags_metadata = [
    {
        "name": "root",
        "description": "Redirects to FastAPI Documentation ",
    }
    ,
    {
        "name": "user/list-users",
        "description": "Endpoint to list users. ",
    },
    {
        "name": "user/register",
        "description": "Register a new user. It asks for admin and persons data. Include validations for identification and registered users",
    },
]


app = FastAPI(
    openapi_tags=tags_metadata,
    title="Fast API MySQL FK",
    description="This is a structured project, with auto docs for the API, validations and more..",
    version="1.0.0",

)
app.include_router(router)