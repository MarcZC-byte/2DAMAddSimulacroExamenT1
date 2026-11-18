import csv


class Alumnos:

    def __init__(self):
        self.nia = None
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.fecha_nacimiento = None

    def leer_alumnos(self):
        # campos = ["nia", "nombre", "apellidos", "email", "fecha_nacimiento"]
        with open("./archivos/alumnos.csv","r",newline="",encoding="utf-8") as f:
            reader = csv.DictReader(f,delimiter=",")
            for alumno in reader:
                print(alumno)

