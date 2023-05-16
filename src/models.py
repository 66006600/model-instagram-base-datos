import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    correo = Column(String(50), nullable=False)
    contrasena = Column(String(50), nullable=False)
    fecha_registro = Column(String(50), nullable=False)

    comments = relationship("Comments", back_populates="user")

    # favorite_character = relationship("Favorite_Character", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    fecha = Column(Integer, nullable=False)
    user = relationship("User", back_populates="posts")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    fecha = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship("User", back_populates= "comments")
    post = relationship("Post", back_populates= "comments")


class Favorit_Post(Base):
    __tablename__ = 'favorit_post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    posts = relationship("Post", back_populates="favorite_post")


class Friend(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    friends_id = Column(Integer, ForeignKey('friends.id'))
    user = relationship(User, back_populates="friends")

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
