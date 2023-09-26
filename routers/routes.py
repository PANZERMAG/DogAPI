import mimetypes
import os.path
import shutil
import uuid
from typing import List

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from controllers.controller import get_pets_db, create_lost_pet, get_posts_db, create_post_db, delete_post, create_user, \
    verif_user
from models import schemes
from models.database import get_db
from models.schemes import Pet, PetCreate, Post, PostCreate, UserCreate, User

router = APIRouter()


@router.get("/photos/{photo_filename}")
async def get_photo(photo_filename: str):
    path = os.path.abspath('../src/img')
    photo_path = os.path.join(path, photo_filename)
    if os.path.exists(photo_path):
        return FileResponse(photo_path)
    else:
        return {"error": "Photo not found"}


@router.get("/get_pets/", response_model=List[schemes.Pet])
def get_all_pets(db: Session = Depends(get_db)):
    pets = get_pets_db(db)
    return pets


@router.get('/get_posts/', response_model=List[schemes.Post])
def get_posts(type_post: str, db: Session = Depends(get_db)):
    print(1)
    print(type_post)
    posts = get_posts_db(type_post, db)
    return posts


@router.post('/lost_pet/', response_model=Pet)
def lost_pet(item: PetCreate, db: Session = Depends(get_db)):
    return create_lost_pet(item=item, db=db)


@router.post('/create_post/', response_model=Post)
def create_post(item: PostCreate, db: Session = Depends(get_db)):
    return create_post_db(item=item, db=db)


@router.post('/upload_photo/')
def upload_photo(photo_file: UploadFile = File(...)):
    type_file = mimetypes.guess_extension(photo_file.content_type)

    path_folder = os.path.abspath("src/img/")

    filename = str(uuid.uuid4()) + str(type_file)

    abs_path = os.path.join(path_folder, filename)

    with open(abs_path, 'wb') as file_photo:
        shutil.copyfileobj(photo_file.file, file_photo)

    return {"path file": str(filename)}


@router.post('/create_user/', )
def create_user_route(item: UserCreate, db: Session = Depends(get_db)):
    return create_user(item, db)


@router.post('/login_user/')
def login_user_route(item: User, db: Session = Depends(get_db)):
    return verif_user(item, db)


@router.delete("/delete_post/")
def delete_post_route(item_id: int, db: Session = Depends(get_db)):
    return delete_post(item_id, db)
