from flaskr import create_app, urls
from flask_restful import Api
from flaskr.vistas import *
from flaskr.modelos import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import logging

def load_context_app(app):
    api = Api(app)    
    api.add_resource(VistaSignUp, urls['VistaSignUp'])
    api.add_resource(VistaLogIn, urls['VistaLogIn'])
    api.add_resource(VistaTarea, urls['VistaTarea'])
    api.add_resource(VistaTareas, urls['VistaTareas'])
    api.add_resource(VistaPing, urls['VistaPing'])
    api.add_resource(VistaEmail, urls['VistaEmail'])
    api.add_resource(VistaArchivos, urls['VistaArchivos'])
    
app = create_app("config/default.py")
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.debug = True


cors = CORS(app)

app_context = app.app_context()
app_context.push()
load_context_app(app)
db.init_app(app)
db.create_all()


jwt = JWTManager(app)
