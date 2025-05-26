# Soy un manco como Yair17, asi que no hay soporte para Linux, sorry
from datetime import datetime
import os, platform, json

class File:
    def __init__(self, file_path: str, exists: bool = True):
        self.file_path = file_path
        self.exists = exists

        if not exists:
            self.creation_date = None
            self.last_modification_date = None
            self.size = 0
            return
        
        # Si quieres agregar... no se, TempleOS, chequea esta linea
        if platform.system() != "Windows":
            raise NotImplementedError("This OS is not supported.")

        stats = os.stat(file_path)
        self.creation_date = datetime.fromtimestamp(stats.st_ctime)
        self.last_modification_date = datetime.fromtimestamp(stats.st_mtime)
        self.size = stats.st_size

    def __repr__(self):
        return (f"<File path='{self.file_path}' exists={self.exists} size={self.size}B "
                f"created={self.creation_date} modified={self.last_modification_date}>")

# Chequea un archivo en singular, devuelve un objeto File (uy que serio :B)
def check_file(file_path: str) -> File: return File(file_path, exists=os.path.exists(file_path))

# Chequea un archivo JSON, devuelve una lista de objetos File
def check_json_file(file_path: str) -> list[File]:
    if not os.path.exists(file_path): return []

    files = []

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

        for item in data:
            folder = item.get("folder")
            if not os.path.exists(folder):
                raise FileNotFoundError(f"Folder {folder} does not exist.")

            for file in item["files"]:
                try: file = eval(file)  # En caso de que tenga una plantilla dinámica tipo f-string
                except: pass
                full_path = os.path.join(folder, file)
                files.append(check_file(full_path))

    return files

# Kingan guli guli guli wacha kingangun kingangun.