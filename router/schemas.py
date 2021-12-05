from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    owner_id: int

class ArticleResponseSchema(ArticleRequestSchema):
    id: int

    class Config:
        orm_mode = True

class OnlyArticleResponseSchema(ArticleRequestSchema):
    pass

    class Config:
        orm_mode = True

class UserRequestSchema(BaseModel):
    username: str
    email: str

class UserResponseSchema(UserRequestSchema):
    id: int

    class Config:
        orm_mode = True

class OnlyUserResponseSchema(UserRequestSchema):
    pass

    class Config:
        orm_mode = True

class CommentRequestSchema(BaseModel):
    username: str
    content: str
    article_id: int
    user_id: int
    
class CommentResponseSchema(CommentRequestSchema):
    id: int

    class Config:
        orm_mode = True

class OnlyCommentResponseSchema(CommentRequestSchema):
    pass

    class Config:
        orm_mode = True

class LikeRequestSchema(BaseModel):
    username: str
    article_id: int
    user_id: int
    
class LikeResponseSchema(LikeRequestSchema):
    id: int

    class Config:
        orm_mode = True

class OnlyLikeResponseSchema(LikeRequestSchema):
    pass

    class Config:
        orm_mode = True


class ArticleResponseWithUserSchema(ArticleRequestSchema):
    id: int
    owner_id: int
    articles_owner: OnlyUserResponseSchema
    articles_comment: List[OnlyCommentResponseSchema] = []
    articles_like: List[OnlyLikeResponseSchema] = []

    class Config:
        orm_mode = True


class UserResponseWithArticleSchema(UserRequestSchema):
    id: int
    created_articles: List[OnlyArticleResponseSchema] = []
    created_comments:  List[OnlyCommentResponseSchema] = []
    created_likes:  List[OnlyLikeResponseSchema] = []

    class Config:
        orm_mode = True


