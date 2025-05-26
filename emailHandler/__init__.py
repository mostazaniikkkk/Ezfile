try: from file import check_json_file  # cuando ya esté instalado como paquete
except ImportError:
    import os
    import sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, ROOT)
    from file import check_json_file  # ahora sí CTM


from email.message import EmailMessage
import smtplib
from .config import EmailConfig
from .html import body

class Email:
    def __init__(self, json_file: str, config: EmailConfig):
        self.files = check_json_file(json_file)
        self.email = EmailMessage()
        self.config = config

    def send(self, title: str, html: str = None, message: str = None):
        self.email['To'] = ', '.join(self.config.to)
        self.email['Subject'] = title
        self.email['From'] = self.config.from_email

        html = body(self.files, html, message)

        self.email.set_content("Tu cliente no soporta HTML.")
        self.email.add_alternative(html, subtype='html')

        with smtplib.SMTP_SSL(self.config.smtp_server, self.config.smtp_port) as smtp:
            smtp.login(self.config.from_email, self.config.password)
            smtp.send_message(self.email)