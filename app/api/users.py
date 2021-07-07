from fastapi import FastAPI,HTTPException
from fastapi import APIRouter
from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import RedirectResponse

from models import modelos,schema
from conexion.Conexion import SessionLocal,engine
from api.crud import users_crud,persons_crud

modelos.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/user'
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/list-users",response_model=List[schema.User],tags=['user/list-users'])
def list(db:Session= Depends(get_db)):
    users = users_crud.list_users(db)
    return users

@router.post("/register", response_model=schema.User, tags=['user/register'])
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_person = persons_crud.get_person_by_identification(db,identification=user.identification)
    if db_person:
        raise HTTPException(status_code=400,detail="Identificación ya registrada")
    db_user = users_crud.get_user_by_username(db,username=user.username)
    if db_user:
        raise HTTPException(status_code=400,detail="Usuario ya existe")
    return users_crud.create_user(db,user=user)





