from .file import check_json_file
from email.message import EmailMessage
import smtplib

class EmailConfig:
    def __init__(self,
                 smtp_server: str,
                 smtp_port: int,
                 from_email: str,
                 password: str,
                 to: list[str]):
        
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password
        self.to = to

class Email:
    def __init__(self, json_file: str, email: EmailMessage, config: EmailConfig):
        self.files = check_json_file(json_file)
        self.email = email
        self.config = config

    def send(self, title: str, body: str):
        self.email['To'] = ', '.join(self.config.to)
        self.email['Subject'] = title
        self.email['From'] = self.config.from_email

        html = f"""<html>
<head><style>
table {{
    width: 100%;
    border-collapse: collapse;
}}
th, td {{
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
    font-family: monospace;
}}
th {{
    background-color: #f2f2f2;
}}
</style></head>
<body>
<p>{body.replace('\n', '<br>')}</p>
<h3>Resumen de archivos</h3>
<table>
<tr>
<th>Archivo</th><th>Existe</th><th>Tamaño (bytes)</th><th>Creado</th><th>Modificado</th>
</tr>
"""

        for file in self.files:
            html += f"<tr><td>{file.file_path}</td><td>{'✅' if file.exists else '❌'}</td>" \
                    f"<td>{file.size}</td><td>{file.creation_date or '-'}</td>" \
                    f"<td>{file.last_modification_date or '-'}</td></tr>"

        html += "</table></body></html>"

        self.email.set_content("Tu cliente no soporta HTML.")
        self.email.add_alternative(html, subtype='html')

        with smtplib.SMTP_SSL(self.config.smtp_server, self.config.smtp_port) as smtp:
            smtp.login(self.config.from_email, self.config.password)
            smtp.send_message(self.email)