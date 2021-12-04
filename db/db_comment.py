from fastapi import HTTPException, status
from router.schemas import CommentRequestSchema
from sqlalchemy.orm.session import Session
from .comment_feed import comment

from db.models import DbComment

def db_feed(db: Session):
    new_comment_list = [DbComment(
        username=comment["username"],
        content=comment["content"],
        article_id=comment["article_id"],
        user_id=comment["user_id"]
    ) for comment in comment]
    db.query(DbComment).delete()
    db.commit()
    db.add_all(new_comment_list)
    db.commit()
    return db.query(DbComment).all()

def create(db: Session, request: CommentRequestSchema) -> DbComment:
    new_comment = DbComment(
        username=request.username,
        content=request.content,
        article_id=request.article_id,
        user_id=request.user_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all(db: Session) -> list[DbComment]:
    return db.query(DbComment).all()