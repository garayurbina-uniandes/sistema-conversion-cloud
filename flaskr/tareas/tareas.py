from datetime import datetime
from celery import Celery
import os
import ffmpeg
from sqlalchemy.sql.functions import func
from ..utils.email import email
from ..modelos import db, Usuario, Estado, Tarea
from flaskr import create_app
from ..utils.botos3 import download_from_s3, upload_to_s3
import logging

celery_app = Celery(__name__, broker=os.environ['REDIS_URL'])

flask_application = create_app("config/default.py")
app_context = flask_application.app_context()
app_context.push()
db.init_app(flask_application)

FFMPEG_BIN = "ffmpeg"
# Statics
UPLOAD_FOLDER = 'files/uploaded'
DOWNLOAD_FOLDER = 'files/download'
EC2_UPLOAD_FOLDER = '/mnt/nfs_clientshare/files/uploaded/'
EC2_DOWNLOAD_FOLDER = '/mnt/nfs_clientshare/files/download/'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg', 'flac'])

@celery_app.task(name="registrar_log")
def registrar_log(usuario, fecha):
    with open('log_signin.txt','a+') as file:
        file.write('{} - inicio de sesión: {} \n'.format(usuario,fecha))

@celery_app.task(name="convertir_archivo")
def convertir_archivo(idTarea):
    with flask_application.app_context():
        tarea  = Tarea.query.get_or_404(idTarea)
        usuario = Usuario.query.get_or_404(tarea.usuario)
        # Convert
        dfile = '{}.{}'.format(os.path.splitext(tarea.file_name)[0], str(tarea.to_format.value)) # Build file name
        inputF = os.path.join(UPLOAD_FOLDER, tarea.file_name) # Build input path
        outputF = os.path.join(DOWNLOAD_FOLDER, dfile) # Build output path and add file
        with open('log_signin.txt','a+') as file:
            file.write(' file_name {} to_format {} outputF {} \n'.format(tarea.file_name,tarea.to_format.value,outputF))
        # Get S3 File
        logging.info('Getting file from S3...')
        download_from_s3(inputF,inputF)
        ffmpeg.input(inputF).output(outputF).overwrite_output().run()
        # Upload to S3 Converted File
        logging.info('Uploading converted file to S3...')
        upload_to_s3(outputF,outputF)
        # enviar_correo(tarea,usuario) desactivado por limitación AWS Academy
        actualizar_estado(tarea)

def enviar_correo(usuario):
  email(usuario)

def actualizar_estado(tarea):
    tarea.estado = Estado.PROCESSED
    tarea.time_completed = func.now()
    db.session.add(tarea)
    db.session.commit()  



    
