import argparse
from email_service import EmailService

def main():
    parser = argparse.ArgumentParser(description="Enviar correos electrónicos")
    parser.add_argument("--to", required=True, help="Correo del destinatario")
    parser.add_argument("--subject", required=True, help="Asunto del correo")
    parser.add_argument("--body", required=True, help="Cuerpo del correo")

    args = parser.parse_args()

    # Crear una instancia del servicio de correo usando el archivo de configuración
    email_service = EmailService()
    success, message = email_service.send_email(args.to, args.subject, args.body)

    if success:
        print("Correo enviado exitosamente")
    else:
        print(f"Error: {message}")

if __name__ == "__main__":
    main()