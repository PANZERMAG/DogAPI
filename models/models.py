from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import FindPetsBD


class Pet(FindPetsBD):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    breed = Column(String, nullable=True)
    chip_number = Column(Integer, nullable=True)
    sex = Column(String, nullable=True)
    pet_color = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    tatoo_number = Column(String, nullable=True)
    weight = Column(Float, nullable=True)


class Post(FindPetsBD):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    desc = Column(String, nullable=True)
    location = Column(String, nullable=True)
    publish_on = Column(String)
    pet_id = Column(Integer(), ForeignKey('pet.id'), nullable=False, unique=True)
    photo = Column(String, nullable=True)
    type_post = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))


class User(FindPetsBD):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    second_name = Column(String)
    email = Column(String, unique=True, nullable=True)
    posts = Column(String)
    password = Column(String)
