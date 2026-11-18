import csv

from Clases.Alumnos import Alumnos
from Clases.Cursos import Cursos
from Clases.Matricula import Matricula


class Academia:

    def __init__(self):
        self.alumnos = Alumnos()
        self.cursos = Cursos()
        self.matriculas = Matricula()

    def cargar_cursos(self):
        self.cursos.insertarCursos()

    def cargar_alumnos(self):
        self.alumnos.insertarAlumnos()

    def cargar_profesores(self):
        return

    def cargar_matriculas(self):
        return

    def mostrar_cursos(self):
        self.cursos.leerCursos()

    def mostrar_alumnos(self):
        self.alumnos.leer_alumnos()

    def mostrar_matriculas(self):
        self.matriculas.leer_matriculas()

    def buscar_alumno(self):
        return

    def modificar_alumno(self):
        return

    def eliminar_alumno(self):
        return

    def generar_import_sql(self):
        return