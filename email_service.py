import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self, config_file="config.json"):
        # Leer la configuración desde el archivo JSON
        with open(config_file, "r") as file:
            config = json.load(file)

        self.smtp_server = config["smtp_server"]
        self.smtp_port = config["smtp_port"]
        self.sender_email = config["sender_email"]
        self.sender_password = config["sender_password"]

    def send_email(self, recipient, subject, body):
        try:
            # Crear el mensaje
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Conectar al servidor SMTP y enviar el correo
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Habilitar cifrado TLS
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient, message.as_string())
            return True, "Correo enviado exitosamente"
        except Exception as e:
            return False, f"Error al enviar el correo: {str(e)}"