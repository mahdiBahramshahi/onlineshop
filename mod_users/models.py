from enum import unique
from sqlalchemy import Column ,Integer , String
from sqlalchemy.sql.expression import column
from app import db
from werkzeug.security import generate_password_hash , check_password_hash

class User(db.Model):
    __tablename__='users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(128),nullable=False, unique=False)
    email = Column(String(128),nullable=False, unique=False)
    password = Column(String(128),nullable=False, unique=False)
    phone_number = Column(String(128),nullable=False, unique=False)
    role = Column(Integer(),nullable=False, default=0)
    
    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password ,password)

    def is_admin(self):
        return self.role == 1


class Blogs(db.Model):
    __tablename__='blog'
    id = Column(Integer(), primary_key=True)
    title = Column(String(128),nullable=False, unique=True)
    image = Column(String(512) , nullable=False , unique= False)
    slug = Column(String(128) , nullable=False , unique= True)
    content = Column(String(3000), nullable=False, unique=False)
    metacontent = Column(String(128), nullable=False, unique=False)
    writer = Column(String(128) , nullable=False , unique= False)
    date = Column(String(32) , nullable=False , unique= False)

