from celery.app.base import Celery
from flask import request
from flask.helpers import flash, send_file
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity
from datetime import datetime

from sqlalchemy.sql.functions import func

from ..utils import email


from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
import base64

from ..modelos import db, Usuario, UsuarioSchema, Tarea, TareaSchema
from sqlalchemy.orm import sessionmaker, Session
import os
import re

usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()

UPLOAD_FOLDER = '../../files/uploaded'
DOWNLOAD_FOLDER = '../../files/download'

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

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
    
    @jwt_required()
    def delete(self,id_tarea):
        tarea = Tarea.query.get_or_404(id_tarea)
        db.session.delete(tarea)
        db.session.commit()
        return {"mensaje": "Tarea {} eliminada exitosamente".format(id_tarea)}

class VistaEmail(Resource):
    def get(self):
        email.email()
        return "Enviado"
    
       

class VistaTareas(Resource):
    @jwt_required() 
    def get(self):
        jwtHeader = get_jwt_identity()
        usuario = jwtHeader
        tarea = Tarea.query.filter(Tarea.usuario == usuario)
        return [tarea_schema.dump(ta) for ta in tarea]

    @jwt_required()
    def post(self):  
        jwtHeader = get_jwt_identity()
        usuario = jwtHeader
        root, extension = os.path.splitext(request.json["fileName"].upper())   
        extension = re.sub("\.","",extension)     
        tarea = Tarea(file_name=request.json["fileName"].upper(),from_format = extension, to_format=request.json["newFormat"].upper(),usuario=usuario, estado= 'UPLOADED',time_created=func.now())
        db.session.add(tarea)
        db.session.commit()
        celery_app.send_task("convertir_archivo", [tarea.id])
        return {"mensaje": "tarea creada exitosamente"}   

class VistaArchivos(Resource):
    def get(self,file_name):
        abs_dir = os.path.dirname(__file__)
        ruta_relativa = os.path.join(UPLOAD_FOLDER, file_name)
        #ruta_relativa = '../../files/uploaded/test.mp3'
        ruta = os.path.join(abs_dir, ruta_relativa)
        try:
            open(ruta)
        except FileNotFoundError:
            ruta_relativa = os.path.join(DOWNLOAD_FOLDER, file_name)
            #ruta_relativa = '../../files/download/test.mp3'
            ruta = os.path.join(abs_dir, ruta_relativa)
            
        archivo_adjunto = ruta.split("/")[-1]
        return send_file(open(ruta, "rb"), attachment_filename=archivo_adjunto)



