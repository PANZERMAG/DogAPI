import os

from sqlalchemy.orm import Session

from models import models
from models.models import Pet, Post, User
from models.schemes import PetCreate, PostCreate, UserCreate


def get_pets_db(db: Session):
    return db.query(models.Pet).all()


def get_posts_db(type_post: str, db: Session):
    print(type_post)
    posts = db.query(models.Post).filter(Post.type_post == type_post).all()
    return posts


def create_lost_pet(item: PetCreate, db: Session):
    db_item = Pet(**item.dict())
    db.add(db_item)
    db.commit()

    return {
        "id": db_item.id,
        "name": db_item.name
    }


def create_post_db(item: PostCreate, db: Session):
    db_item = Post(**item.dict())
    db.add(db_item)
    db.commit()

    return {
        "id": db_item.id,
        "pet_id": db_item.pet_id,
        "photo": db_item.photo,
        "publish_on": db_item.publish_on,
        "type_post": db_item.type_post
    }


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
    db.add(db_item)
    db.commit()

    return {
        "status": "Account has beem successfull created"
    }


def verif_user(item: User, db: Session):
    db_item = db.query(User).filter(User.email == item.email).filter(User.password == item.password).first()

    if db_item:
        return {
            "Response": "User true"
        }
    return {
        "Response": "User not true"
    }
