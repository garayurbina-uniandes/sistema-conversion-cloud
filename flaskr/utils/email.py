import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ..modelos.modelos import Tarea, Usuario

email_destino = "recursosimp@gmail.com"

def email(tarea: Tarea,usuario: Usuario):

    username = email_destino
    password = "pepesitos"
    mail_from = email_destino
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


def emailSecond(tarea: Tarea,usuario: Usuario):

    username = email_destino
    password = "pepesitos"
    mail_from = email_destino
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

def email_third(tarea: Tarea,usuario: Usuario):

    username = email_destino
    password = "pepesitos"
    mail_from = email_destino
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
