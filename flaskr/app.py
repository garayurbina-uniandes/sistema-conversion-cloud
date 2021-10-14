from flaskr import create_app, urls
from flask_restful import Api
from .modelos import db
from .vistas import VistaSignUp, VistaLogIn
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def load_context_app(app):
    api = Api(app)    
    api.add_resource(VistaSignUp, urls['VistaSignUp'])
    api.add_resource(VistaLogIn, urls['VistaLogIn'])
    
app = create_app("config/default.py")
app_context = app.app_context()
app_context.push()
load_context_app(app)


db.init_app(app)
db.create_all()
cors = CORS(app)



jwt = JWTManager(app)
