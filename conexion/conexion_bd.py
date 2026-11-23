import mysql.connector

from mysql.connector import errorcode

from conexion.dbconfig import DB_CONFIG

class ConexionBD:

    def __init__(self):
        self.cnx = None

    def __enter__(self):
        try:
            self.cnx = mysql.connector.connect(**DB_CONFIG)
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