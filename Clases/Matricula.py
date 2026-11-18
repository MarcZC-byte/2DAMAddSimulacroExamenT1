import csv
from dataclasses import fields
from idlelib.iomenu import encoding


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
            for matricula in reader:
                print(matricula)