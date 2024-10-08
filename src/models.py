import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

'''class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)'''

class User(Base):
    __tablename__ = 'user'
    id=Column(Integer,primary_key=True)
    username = Column(String(60),nullable=False)
    first_name = Column(String(60))
    last_name = Column(String(60))
    email = Column(String(60))

class Comment(Base):
    __tablename__ = 'comment'
    id=Column(Integer,primary_key=True)
    comment_text =  Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))    

class Media(Base):
    __tablename__ = 'media'
    id=Column(Integer,primary_key=True)
    type = Column(String(60))    
    url = Column(String(125))
    post_id = Column(Integer, ForeignKey('post.id'))

class Fallower(Base):
    __tablename__ = 'fallower'
    id=Column(Integer,primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))  
    user_to_id = Column(Integer, ForeignKey('user.id'))  
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
