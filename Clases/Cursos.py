
class Cursos:

    def __init__(self):
        self.curso_id = None
        self.nombre = None
        self.duracion_horas = None
        self.precio = None

    def leerCursos(self):
        with open("./archivos/cursos.xml", "r", encoding="utf-8") as f:

