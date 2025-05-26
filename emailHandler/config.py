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