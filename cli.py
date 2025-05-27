import argparse, json
from email_handler import *

# Gestiona el ARGS
parser = argparse.ArgumentParser(
    prog="Ez-Watcher",
    description="CLI tool designed to audit and report the status of generated files via email."
)

parser.add_argument("--config", required=True, help="Path to the SMTP config file")
parser.add_argument("--folders", required=True, help="Path to the folder list file")

args = parser.parse_args()

# Revisa los archivos de configuración y carpetas
try:
    config = args.config if args.config else "config.json"
    folders = args.folders if args.folders else "folders.json"
except Exception as e:
    print(f"Error parsing arguments: {e}")
    exit(1)

with open(config, "r") as f:
    try: smtp_config = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading SMTP config file: {e}")
        exit(1)

config = EmailConfig(
    smtp_server=smtp_config["smtp"]["smtp_server"],
    smtp_port=smtp_config["smtp"]["smtp_port"],
    from_email=smtp_config["smtp"]["from_email"],
    password=smtp_config["smtp"]["password"],
    to=smtp_config["smtp"]["to"]
)

email = Email("example.json", config)
email.send(
    title=smtp_config["email"]["subject"],
    message=smtp_config["email"]["body"]
)