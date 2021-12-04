from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    articles_owner = relationship('DbUser', back_populates ='created_articles')
    articles_comment =  relationship('DbComment', back_populates ='comments_article')
    articles_like =  relationship('DbLike', back_populates ='likes_article')

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    created_articles = relationship('DbArticle', back_populates='articles_owner')
    created_comments =  relationship('DbComment', back_populates ='comments_user')
    created_likes =  relationship('DbLike', back_populates ='likes_user')

class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    content = Column(String)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comments_article = relationship('DbArticle', back_populates='articles_comment')
    comments_user = relationship('DbUser', back_populates='created_comments')

class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    likes_article = relationship('DbArticle', back_populates='articles_like')
    likes_user = relationship('DbUser', back_populates='created_likes')