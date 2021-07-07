from fastapi import FastAPI
from fastapi import APIRouter
from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import RedirectResponse

from models import modelos,schema
from conexion.Conexion import SessionLocal,engine

modelos.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/")
def root():
    return RedirectResponse(url="/docs/")









