from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import LikeRequestSchema, LikeResponseSchema
from db.database import get_db
from db import db_like
from typing import List

router = APIRouter(
    prefix='/api/v1/likes',
    tags=['likes']
)


@router.post('', response_model=LikeResponseSchema)
def create(request: LikeRequestSchema, db: Session = Depends(get_db)):
    return db_like.create(db=db, request=request)


@router.get('/feed', response_model=List[LikeResponseSchema])
def get_all_likes(db: Session = Depends(get_db)):
    return db_like.db_feed(db)


@router.get('/all', response_model=List[LikeResponseSchema])
def get_all_likes(db: Session = Depends(get_db)):
    return db_like.get_all(db)