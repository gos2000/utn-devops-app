import unittest
from unittest.mock import patch, mock_open
from email_service import EmailService

class TestEmailService(unittest.TestCase):
    @patch('smtplib.SMTP')
    @patch('builtins.open', new_callable=mock_open, read_data='{"smtp_server": "smtp.test.com", "smtp_port": 587, "sender_email": "test@example.com", "sender_password": "password"}')
    def test_send_email_success(self, mock_file, mock_smtp):
        # Configurar el mock del servidor SMTP
        mock_smtp.return_value.__enter__.return_value = mock_smtp

        # Crear una instancia del servicio de correo
        email_service = EmailService()

        # Simular el envío de un correo
        success, message = email_service.send_email("recipient@example.com", "Test Subject", "Test Body")

        # Verificar que el correo se haya enviado correctamente
        self.assertTrue(success)
        self.assertEqual(message, "Correo enviado exitosamente")
        mock_smtp.assert_called_once()

    @patch('smtplib.SMTP')
    @patch('builtins.open', new_callable=mock_open, read_data='{"smtp_server": "smtp.test.com", "smtp_port": 587, "sender_email": "test@example.com", "sender_password": "password"}')
    def test_send_email_failure(self, mock_file, mock_smtp):
        # Configurar el mock del servidor SMTP para lanzar una excepción
        mock_smtp.side_effect = Exception("Error simulado")

        # Crear una instancia del servicio de correo
        email_service = EmailService()

        # Simular el envío de un correo
        success, message = email_service.send_email("recipient@example.com", "Test Subject", "Test Body")

        # Verificar que el correo no se haya enviado
        self.assertFalse(success)
        self.assertIn("Error al enviar el correo", message)

if __name__ == "__main__":
    unittest.main()