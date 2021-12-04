from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import CommentRequestSchema, CommentResponseSchema
from db.database import get_db
from db import db_comment
from typing import List

router = APIRouter(
    prefix='/api/v1/comments',
    tags=['comments']
)


@router.post('', response_model=CommentResponseSchema)
def create(request: CommentRequestSchema, db: Session = Depends(get_db)):
    return db_comment.create(db=db, request=request)


@router.get('/feed', response_model=List[CommentResponseSchema])
def get_all_comments(db: Session = Depends(get_db)):
    return db_comment.db_feed(db)


@router.get('/all', response_model=List[CommentResponseSchema])
def get_all_comments(db: Session = Depends(get_db)):
    return db_comment.get_all(db)
