from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from models.database import get_db
from models.models import AccessKey

api_key_header = APIKeyHeader(name="X-API-Key")


def get_current_user(api_key: str = Depends(api_key_header), db: Session = Depends(get_db)):
    api_key_db = db.query(AccessKey).filter(AccessKey.key == api_key).first()
    if api_key_db:
        return api_key_db.key
    return HTTPException(status_code=401, detail="Invalid API Key")
