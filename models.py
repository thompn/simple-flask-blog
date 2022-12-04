from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    body = Column(String, nullable=False)
    image = Column(String(128))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title, body, created_at, image=None):
        self.title = title
        self.body = body
        self.created_at = created_at
        self.image = image

    @classmethod
    def all(cls):
        session = Session()
        posts = session.query(Post).order_by(Post.created_at.desc()).all()  # Update the query to include the image column
        session.close()
        return posts

    @classmethod
    def create(cls, title, body, image):
        session = Session()
        post = cls(title=title, body=body, created_at=datetime.utcnow(), image=image)
        session.add(post)
        session.commit()
        session.close()
        return post

    @classmethod
    def get(cls, id):
        session = Session()
        post = session.query(cls).filter(cls.id == id).one()
        session.close()
        return post

    def save(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()

    def __repr__(self):
        return f'<Post(id={self.id}, title={self.title}, body={self.body}, created_at={self.created_at})>'

engine = create_engine('sqlite:///posts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
