import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from re import findall
from subprocess import Popen, PIPE

def send_email(subject, body, to_email):
    # Configura la conexión al servidor SMTP de tu proveedor de correo
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'email'
    smtp_password = 'clave de aplicación'

    # Configura el mensaje de correo electrónico
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Establece la conexión y envía el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

def ping (host,ping_count):
     # Lista de direcciones de correo electrónico a las que se enviará el correo en caso de fallo
    email_recipients = ['email1_copy', 'email2_copy'] #añadir los que se consideren necesarios

    for ip in host:
        data = ""
        output= Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8", errors='ignore')
     

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{ip} : Successful Ping")
        else:
            subject = 'Asunto del mensaje'
            body = f'cuerpo del mensaje.'
        
            for recipient in email_recipients:
                send_email(subject, body, recipient)
            
            
nodes = ["ip o url a testear"]

if __name__ == "__main__":
    ping(nodes,3)
