from pydantic import BaseModel


# ----Pet models
class PetBase(BaseModel):
    breed: str


class PetCreate(PetBase):
    breed: str
    chip_number: str
    pet_color: str
    age: int
    tatoo_number: str
    weight: float


class Pet(PetBase):
    id: int
    chip_number: str
    pet_color: str
    age: int
    tatoo_number: str
    weight: float

    class Config:
        orm_mode = True


# ------Post models
class PostBase(BaseModel):
    pet_id: int


class PostCreate(PostBase):
    name: str
    type_post: str
    desc: str
    location: str
    photo: str
    publish_on: str
    user_id: int


class Post(PostBase):
    name: str
    id: int
    pet_id: int
    photo: str
    publish_on: str
    type_post: str
    location: str

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
