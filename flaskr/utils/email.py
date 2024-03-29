import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ..modelos.modelos import Tarea, Usuario

email_destino = "recursosimp@gmail.com"
email_subject = "Conversión lista"
mail_body_end = " su archivo convertido está listo para ser descargado"
estimado ="Estimado "
smtp = "smtp.gmail.com"
password = os.environ.get("EMAIL_PASSWORD")

def email(usuario: Usuario):

    username = email_destino
    mail_from = email_destino
    mail_to = usuario.email
    mail_subject = email_subject
    mail_body = Estimado + usuario.username + mail_body_end

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host=smtp, port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()


def emailSecond(tarea: Tarea,usuario: Usuario):

    username = email_destino
    mail_from = email_destino
    mail_to = usuario.email
    mail_subject = email_subject
    mail_body = Estimado + usuario.username + mail_body_end

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host=smtp, port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()

def email_third(tarea: Tarea,usuario: Usuario):

    username = email_destino

    mail_from = email_destino
    mail_to = usuario.email
    mail_subject = email_subject
    mail_body = Estimado + usuario.username + mail_body_end

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host=smtp, port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()
