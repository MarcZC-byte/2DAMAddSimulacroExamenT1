import csv
from dataclasses import fields

from conexion.conexion_bd import ConexionBD


class Matricula:

    def __init__(self):
        self.matricula_id = None
        self.nia = None
        self.curso_id = None
        self.fecha_matricula = None
        self.nota = None

    def leer_matriculas(self):

        with open("./archivos/matriculas.csv", "r",encoding="utf-8") as f:
            reader = csv.DictReader(f,delimiter=",")
            matriculas = list(reader)
            for m in matriculas:
                print(m)
            return matriculas

    def insertarMatriculas(self):

        consulta= (
            "INSERT INTO matricula (nia,curso_id,fecha_matricula,nota)"
            "VALUES (%s,%s,%s,%s)"
        )
        with ConexionBD() as cnx:
            cursor = cnx.cursor()

            for matricula in self.leer_matriculas():
                valores = (
                    matricula["nia"],
                    matricula["curso_id"],
                    matricula["fecha_matricula"],
                    matricula["nota"]
                )
                cursor.execute(consulta,valores)
            cnx.commit()
            cursor.close()
        print("Insertados con exito")