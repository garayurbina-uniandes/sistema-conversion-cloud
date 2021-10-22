from . import create_app, urls
from flask_restful import Api
from .vistas import *
from .modelos import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

def load_context_app(app):
    api = Api(app)    
    api.add_resource(VistaSignUp, urls['VistaSignUp'])
    api.add_resource(VistaLogIn, urls['VistaLogIn'])
    api.add_resource(VistaTarea, urls['VistaTarea'])
    api.add_resource(VistaTareas, urls['VistaTareas'])
    api.add_resource(VistaPing, urls['VistaPing'])
    api.add_resource(VistaEmail, urls['VistaEmail'])
    
app = create_app("config/default.py")


cors = CORS(app)

app_context = app.app_context()
app_context.push()
load_context_app(app)
db.init_app(app)
db.create_all()


jwt = JWTManager(app)
