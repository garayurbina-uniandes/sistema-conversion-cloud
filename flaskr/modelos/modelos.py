import enum
from sqlalchemy.sql.functions import func

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum


Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    username =  Column(String(50), unique=True, nullable=False)
    password1 =  Column(String(50), nullable=False)
    password2 =  Column(String(50), nullable=False)

class Estado(enum.Enum):
   UPLOADED = 'uploaded'
   PROCESSED = 'processed'

class Medio(enum.Enum):
   MP3 = 'MP3'
   ACC = 'ACC'
   OGG = 'OGG'
   WAV = 'WAV'
   WMA = 'WMA'

class Tarea(Base):
    __tablename__ = 'tarea'
    id = Column(Integer, primary_key=True)
    usuario = Column(Integer, ForeignKey("usuario.id"))
    estado = Column(Enum(Estado))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_completed = Column(DateTime(timezone=True), onupdate=func.now())
    from_format = Column(Enum(Medio))
    to_format = Column(Enum(Medio))
   


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class TareaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        include_relationships = True
        load_instance = True


