import csv

from conexion.conexion_bd import ConexionBD


class Profesor:

    def __init__(self):
        self.profesor_id = None
        self.nombre = None
        self.apellidos = None
        self.especialidad = None

    def leerProfesores(self):
        with open("./archivos/profesores.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f,delimiter=",")
            profesores = list(reader)

            for p in profesores:
                print(p)
            return profesores

    def insertarProfesores(self):
        consulta = (
            "INSERT INTO profesor (nombre,apellidos,especialidad)"
            "VALUE (%s,%s,%s)"
        )
        with ConexionBD() as cnx:
            cursor = cnx.cursor()

            for profesor in self.leerProfesores():
                valores = (
                    profesor["nombre"],
                    profesor["apellidos"],
                    profesor["especialidad"]
                )
                cursor.execute(consulta,valores)
            cnx.commit()
            cursor.close()
        print("Insertados correctamente")