from pydantic import BaseModel


# ----Pet models
class PetBase(BaseModel):
    breed: str


class PetCreate(PetBase):
    ...

class Pet(PetBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# ------Post models
class PostBase(BaseModel):
    name: str
    pet_id: int


class PostCreate(PostBase):
    type_post: str
    desc: str
    location: str
    photo: str
    publish_on: str
    user_id: int


class Post(PostBase):
    id: int
    pet_id: int
    photo: str
    publish_on: str
    type_post: str

    class Config:
        orm_mode = True


# ----- User model
class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    first_name: str
    second_name: str
    email: str
    password: str


class User(UserBase):
    email: str
    password: str

    class Config:
        orm_mode = True
