import enum

from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    username =  Column(String(50), unique=True, nullable=False)
    password1 =  Column(String(50), nullable=False)
    password2 =  Column(String(50), nullable=False)
   


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True


