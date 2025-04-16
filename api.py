from flask import Flask, request, jsonify
from email_service import EmailService

app = Flask(__name__)

# Crear una instancia del servicio de correo usando el archivo de configuración
email_service = EmailService()

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    if not recipient or not subject or not body:
        return jsonify({"error": "Faltan parámetros"}), 400

    success, message = email_service.send_email(recipient, subject, body)
    if success:
        return jsonify({"message": "Correo enviado exitosamente"}), 200
    else:
        return jsonify({"error": message}), 500

if __name__ == "__main__":
    app.run(debug=True)