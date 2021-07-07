from typing import List, Optional
from pydantic import BaseModel



'''
schemas for person model
'''



class PersonBase(BaseModel):

    names:str
    last_names:str
    identification:str
    gender:str
    class Config:
        orm_mode = True

class PersonCreate(PersonBase):
    pass
    class Config:
        orm_mode = True


class Person(PersonBase):
    id:Optional[int]
    status:bool
    class Config:
        orm_mode = True




'''
schemas for user model
'''


class UserBase(BaseModel):
    username : str
    #person_id : int

class UserCreate(UserBase):
    names:str
    last_names:str
    identification:str
    gender:str
    password : str

class User(UserBase):
    id : int
    status : int
    person:Person={}
    
    class Config:
        orm_mode = True
