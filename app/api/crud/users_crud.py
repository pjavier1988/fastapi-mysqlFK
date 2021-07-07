from sqlalchemy.orm import Session
from fastapi.params import Depends
from models import modelos,schema
from api.crud import persons_crud




def create_user(db: Session, user: schema.UserCreate):
    try:
        person = modelos.Person(names=user.names, last_names=user.last_names, identification=user.identification)
    except ValidationError as e:
        return modelos.User()
    db_person =persons_crud.create_person(db,person=person)
    if db_person:
        db_user = modelos.User(username=user.username, password=user.password, person_id=db_person.id)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user

def list_users(db:Session):
    users = db.query(modelos.User).all()
    return users


def get_user_by_username(db: Session, username: str):
    return db.query(modelos.User).filter(modelos.User.username == username).first()