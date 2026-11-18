import os
import mysql.connector

from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv()


class ConexionBD:

    DB_CONFIG = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "33006")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "dbrootpass"),
        "database": os.getenv("DB_NAME", "claseSimulacro"),
    }

    def __init__(self):
        self.cnx = None

    def __enter__(self):
        try:
            self.cnx = mysql.connector.connect(**self.DB_CONFIG)
            return self.cnx

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise RuntimeError("Usuario o contraseña incorrectos") from err

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise RuntimeError("La base de datos no existe") from err

            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cnx is not None and self.cnx.is_connected():
            self.cnx.close()