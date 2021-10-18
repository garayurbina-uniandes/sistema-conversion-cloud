from flask import request
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from ..modelos import db, Usuario, UsuarioSchema, Tarea, TareaSchema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()


class VistaSignUp(Resource):

    def post(self):
        usuario_username = Usuario.query.filter(Usuario.username == request.json["username"]).first()
        usuario_email = Usuario.query.filter(Usuario.email == request.json["email"]).first()
        db.session.commit()
        if usuario_username is None and usuario_email is None:                
            nuevo_usuario = Usuario(email=request.json["email"], username=request.json["username"], password1=request.json["password1"],password2=request.json["password2"])
            db.session.add(nuevo_usuario)
            db.session.commit()
            token_de_acceso = create_access_token(identity=nuevo_usuario.id)
            return {"mensaje": "usuario creado exitosamente", "token": token_de_acceso}
        else:
            return "El usuario ya existe"


class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.username == request.json["username"],
                                       Usuario.password1 == request.json["password"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}

class VistaTarea(Resource):
    @jwt_required()
    def get(self,id_tarea):
        return tarea_schema.dump(Tarea.query.get_or_404(id_tarea))



