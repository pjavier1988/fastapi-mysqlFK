from fastapi import FastAPI,HTTPException
from fastapi import APIRouter
from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import RedirectResponse

from api.crud import persons_crud
from models import modelos,schema
from conexion.Conexion import SessionLocal,engine


modelos.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/person'
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/list-person",response_model=List[schema.Person])
def list_persons(db:Session= Depends(get_db)):
    persons = persons_crud.list_persons(db)
    return persons

@router.post("/persons/", response_model=schema.Person)
def create_user(person: schema.PersonCreate, db: Session = Depends(get_db)):
    db_person = persons_crud.get_person_by_identification(db,identification=person.identification)
    if db_person:
        raise HTTPException(status_code=400,detail="Identificación ya registrada")
    return persons_crud.create_person(db,person=person)





