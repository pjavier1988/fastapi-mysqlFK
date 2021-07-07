from sqlalchemy.orm import Session
from fastapi.params import Depends
from models import modelos,schema



def create_person(db: Session, person: schema.PersonCreate):

    db_person = modelos.Person(names=person.names, last_names=person.last_names, identification=person.identification,gender=person.gender)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def list_persons(db:Session):
    persons = db.query(modelos.Person).all()
    return persons


def get_person_by_identification(db: Session, identification: str):
    return db.query(modelos.Person).filter(modelos.Person.identification == identification).first()