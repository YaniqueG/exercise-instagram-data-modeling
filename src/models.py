import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer,ForeignKey('Comment.author_id'),ForeignKey('Post.user_id'),primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True)

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer,ForeignKey('Comment.post_id'),primary_key=True)
    user_id =Column(Integer,ForeignKey('User.id'))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    media_type = Column(Integer)
    url = Column(String(250))
    post_id = Column(String(250),ForeignKey('Post.id'))

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,ForeignKey('User.id'))
    user_to_id = Column(Integer,ForeignKey('User.id'))
    
class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(String(250),primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)




    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
