from sqlalchemy import Column , Integer , String , Text
from app import db

class Mahsolat(db.Model):
    __tablename__='mahsolat'
    id = Column(Integer , primary_key=True)
    title = Column(String(128) , nullable=False , unique= False)
    description = Column(String(256) , nullable=False , unique= False)
    slug = Column(String(128) , nullable=False , unique= True)
    group = Column(String(128) , nullable=False , unique= False)
    price = Column(String(128) , nullable=False , unique= False)
    image = Column(String(128) , nullable=False , unique=False)

