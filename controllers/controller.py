import os
import uuid

from sqlalchemy.orm import Session

from models import models
from models.models import Pet, Post, User, AccessKey
from models.schemes import PetCreate, PostCreate, UserCreate


def get_pets_db(db: Session):
    return db.query(models.Pet).all()

def get_pet_db(pet_id, db: Session):
    pet = db.query(models.Pet).filter(Pet.id == pet_id).first()
    return pet



def get_posts_db(type_post: str, db: Session):
    print(type_post)
    posts = db.query(models.Post).filter(Post.type_post == type_post).all()
    return posts


def create_lost_pet(item: PetCreate, db: Session):
    db_item = Pet(**item.dict())
    db.add(db_item)
    db.commit()

    return db_item


def create_post_db(item: PostCreate, db: Session):
    db_item = Post(**item.dict())
    db.add(db_item)
    db.commit()

    return db_item


def delete_post(item_id: int, db: Session):
    item = db.query(Post).filter(Post.pet_id == item_id).first()

    pet_item = db.query(Pet).filter(Pet.id == item_id).first()

    os.remove(Pet.photo)

    db.delete(pet_item)
    db.delete(item)
    db.commit()

    return {
        "Status": "Successfully delete"
    }


def create_user(item: UserCreate, db: Session):

    db_item = User(**item.dict())

    db_key = AccessKey(key=str(uuid.uuid4()))


    db.add(db_item)
    db.add(db_key)
    db.commit()

    return {
        "status": True,
        "key": db_key.key
    }


def verif_user(item: User, db: Session):
    db_item = db.query(User).filter(User.email == item.email).filter(User.password == item.password).first()

    if db_item:
        return {
            "Response": True
        }
    return {
        "Response": False
    }
