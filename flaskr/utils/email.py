import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ..modelos.modelos import Tarea, Usuario

def email(tarea: Tarea,usuario: Usuario):

    username = "recursosimp@gmail.com"
    password = "pepesitos"
    mail_from = "recursosimp@gmail.com"
    mail_to = usuario.email
    mail_subject = "Conversión lista"
    mail_body = "Estimado " + usuario.username + " su archivo convertido está listo para ser descargado"

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()