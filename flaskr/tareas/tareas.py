from celery import Celery
import os
import subprocess as sp

from werkzeug.utils import secure_filename

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

FFMPEG_BIN = "ffmpeg"
# Statics
UPLOAD_FOLDER = 'files\\uploaded'
DOWNLOAD_FOLDER = 'files\\download'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg', 'flac'])

@celery_app.task()
def registrar_log(usuario, fecha):
    with open('log_signin.txt','a+') as file:
        file.write('{} - inicio de sesión: {} \n'.format(usuario,fecha))

@celery_app.task()
def convertir_archivo(location,newFormat):
    file = open('test.mp3')
    format = 'wav'
    filename = secure_filename(file.name)
    # Convert
    dfile = '{}.{}'.format(os.path.splitext(filename)[0], str(format)) # Build file name
    inputF = os.path.join(UPLOAD_FOLDER, file.name) # Build input path
    outputF = os.path.join(DOWNLOAD_FOLDER, dfile) # Build output path and add file
    convertCMD = [FFMPEG_BIN, '-y', '-i', 'test.mp3', 'test.wav'] # Ffmpeg is flexible enough to handle wildstar conversions

    with open('log_signin.txt','a+') as file:
        file.write('{} - Comando de ejecucion: {} \n'.format('logJose',convertCMD))

    executeOrder66 = sp.call(convertCMD, shell = True)