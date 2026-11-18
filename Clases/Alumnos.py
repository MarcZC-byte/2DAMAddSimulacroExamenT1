import csv
from dataclasses import fields

from conexion.conexion_bd import ConexionBD


class Alumnos:

    def __init__(self):
        self.nia = None
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.fecha_nacimiento = None

    def leer_alumnos(self):
        # campos = ["nia", "nombre", "apellidos", "email", "fecha_nacimiento"]
        with open("./archivos/alumnos.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            alumnos = list(reader)
            for alumno in reader:
                print(alumno)
            return alumnos

    def insertarAlumnos(self):
        consulta = (
            "INSERT INTO alumno (nia, nombre, apellidos, email, fecha_nacimiento) "
            "VALUES (%s,%s,%s,%s,%s)"
        )
        with ConexionBD() as cnx:
            cursor = cnx.cursor()
            for alumno in self.leer_alumnos():
                cursor.execute(consulta,(
                               alumno["nia"],
                               alumno["nombre"],
                               alumno["apellidos"],
                               alumno["email"],
                               alumno["fecha_nacimiento"])
                               )
                cnx.commit()
            cursor.close()

        print("Insertados correctamente")