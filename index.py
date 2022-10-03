import smtplib
import ssl
from email.message import EmailMessage
import csv

email_sender = 'username@udesa.edu.ar'
email_password = 'APP PASSWROD'
subject = 'Nota parcial'
body = """
"""

receivers = []
with open("./receivers.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        receivers.append(row)
for r in receivers:
    email_receiver = r[0]
    body = f"""
    Hola, 
    tu nota en el examen fue:{r[1]}
    Saludos,
    Cristian"""
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
