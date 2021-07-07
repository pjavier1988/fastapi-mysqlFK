

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer,String
from sqlalchemy.orm import relationship
from conexion.Conexion import Base


'''
Clase para el mapeo de la tabla usuario
'''




class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True,index=True)
    names = Column(String(20))
    last_names = Column(String(200))
    identification = Column(String(13))
    gender = Column(String(1))
    status = Column(Integer,default=1)
    user = relationship("User",back_populates="person", uselist=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    password = Column(String(200))
    status = Column(Integer,default=1)
    person_id = Column(Integer,ForeignKey('person.id'))
    person = relationship("Person",back_populates="user")
    profile = relationship("Profile",back_populates="user_profile", uselist=False)
    


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    payment_method = Column(String(20))
    user_profile = relationship("User",back_populates="profile", uselist=False)
    




