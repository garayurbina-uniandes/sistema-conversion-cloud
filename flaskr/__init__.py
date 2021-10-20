from flask import Flask

urls = { 'VistaSignUp': '/api/auth/signup', 
         'VistaLogIn': '/api/auth/login',
         'VistaTarea': '/api/tasks/<int:id_tarea>',
         'VistaTareas': '/api/tasks'
        }


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_pyfile(config_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app