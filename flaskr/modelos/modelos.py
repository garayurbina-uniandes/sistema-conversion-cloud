import enum
from sqlalchemy.sql.functions import func

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username =  db.Column(db.String(50), unique=True, nullable=False)
    password1 =  db.Column(db.String(50), nullable=False)
    password2 =  db.Column(db.String(50), nullable=False)

class Estado(enum.Enum):
   UPLOADED = 'uploaded'
   PROCESSED = 'processed'

class Medio(enum.Enum):
   MP3 = 'MP3'
   ACC = 'ACC'
   OGG = 'OGG'
   WAV = 'WAV'
   WMA = 'WMA'

class Tarea(db.Model):
    __tablename__ = 'tarea'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, ForeignKey("usuario.id"))
    estado = db.Column(db.Enum(Estado))
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_completed = db.Column(DateTime(timezone=True), onupdate=func.now())
    from_format = db.Column(db.Enum(Medio))
    to_format = db.Column(db.Enum(Medio))
   


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


