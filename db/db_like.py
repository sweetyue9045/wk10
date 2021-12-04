from fastapi import HTTPException, status
from router.schemas import LikeRequestSchema
from sqlalchemy.orm.session import Session
from .like_feed import like

from db.models import DbLike

def db_feed(db: Session):
    new_like_list = [DbLike(
        username=like["username"],
        article_id=like["article_id"],
        user_id=like["user_id"]
    ) for like in like]
    db.query(DbLike).delete()
    db.commit()
    db.add_all(new_like_list)
    db.commit()
    return db.query(DbLike).all()

def create(db: Session, request: LikeRequestSchema) -> DbLike:
    new_like = DbLike(
        username=request.username,
        article_id=request.article_id,
        user_id=request.user_id
    )
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like

def get_all(db: Session) -> list[DbLike]:
    return db.query(DbLike).all()