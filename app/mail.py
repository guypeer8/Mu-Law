import os
import sendgrid

def send_email(subject, body):
    mail = os.environ.get('MAIL_USERNAME')
    sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_APIKEY'))
    message = sendgrid.Mail(to=mail, subject=subject, html=body, text=body, from_email=mail)
    sg.send(message)
