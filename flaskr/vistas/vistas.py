from flask import request
from flask.helpers import flash
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity
from datetime import datetime


from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
import base64

from ..modelos import db, Usuario, UsuarioSchema, Tarea, TareaSchema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from flask import jsonify



usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()

class VistaPing(Resource):
    def get(self):
        return("Pong")

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

    @jwt_required()
    def put(self,id_tarea):
        tarea = Tarea.query.get_or_404(id_tarea)
        tarea.to_format = request.json.get("to_format", tarea.to_format)
        db.session.commit()
        return tarea_schema.dump(tarea)

    
       

class VistaTareas(Resource):
    @jwt_required()
    def get(self):
        tarea = Tarea.query.all()
        return [tarea_schema.dump(ta) for ta in tarea]

    @jwt_required()
    def post(self):  
        jwtHeader = get_jwt_identity()
        usuario = jwtHeader
        print(usuario)
        tarea = Tarea(from_format=request.json["fileName"].upper(), to_format=request.json["newFormat"].upper(),usuario=usuario, estado= 'UPLOADED',time_completed=datetime.today().strftime('%Y-%m-%d %H:%M'))
        db.session.add(tarea)
        db.session.commit()
        return {"mensaje": "tarea creada exitosamente"}   


