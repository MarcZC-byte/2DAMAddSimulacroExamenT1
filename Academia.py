from Clases.Alumnos import Alumnos
from Clases.Cursos import Cursos
from Clases.Matricula import Matricula
from Clases.Profesor import Profesor


class Academia:

    def __init__(self):
        self.alumnos = Alumnos()
        self.cursos = Cursos()
        self.matriculas = Matricula()
        self.profesores = Profesor()

    def cargar_cursos(self):
        self.cursos.insertarCursos()

    def cargar_alumnos(self):
        self.alumnos.insertarAlumnos()

    def cargar_profesores(self):
        self.profesores.insertarProfesores()

    def cargar_matriculas(self):
        self.matriculas.insertarMatriculas()

    def mostrar_cursos(self):
        self.cursos.leerCursos()

    def mostrar_alumnos(self):
        self.alumnos.leer_alumnos()

    def mostrar_matriculas(self):
        self.matriculas.leer_matriculas()

    def buscar_alumno(self):
        self.alumnos.buscarAlumno("1001")

    def modificar_alumno(self):
        self.alumnos.modificar_alumno("1001")

    def eliminar_alumno(self):
        self.alumnos.eliminar_alumno("1001")

    def generar_import_sql(self):
        with open("./archivos/import.sql", "w", encoding="utf-8") as f:
            # ALUMNOS
            alumnos = self.alumnos.leer_alumnos()

            for alumno in alumnos:
                consulta = (
                    "INSERT INTO alumno "
                    "(nia, nombre, apellidos, email, fecha_nacimiento) "
                    "VALUES "
                    f"('{alumno['nia']}', '{alumno['nombre']}', "
                    f"'{alumno['apellidos']}', '{alumno['email']}', "
                    f"'{alumno['fecha_nacimiento']}');\n"
                )
                f.write(consulta)

            # CURSOS
            cursos = self.cursos.leerCursos()

            for curso in cursos:
                consulta = (
                    "INSERT INTO curso "
                    "(nombre, duracion_horas, precio) "
                    "VALUES "
                    f"('{curso['nombre']}', "
                    f"'{curso['duracion_horas']}', "
                    f"'{curso['precio']}');\n"
                )
                f.write(consulta)

            # MATRICULAS
            matriculas = self.matriculas.leer_matriculas()

            for matricula in matriculas:
                consulta = (
                    "INSERT INTO matricula "
                    "(nia, curso_id, fecha_matricula, nota) "
                    "VALUES "
                    f"('{matricula['nia']}', "
                    f"'{matricula['curso_id']}', "
                    f"'{matricula['fecha_matricula']}', "
                    f"'{matricula['nota']}');\n"
                )
                f.write(consulta)

            # PROFESORES
            profesores = self.profesores.leerProfesores()

            for profesor in profesores:
                consulta = (
                    "INSERT INTO profesor "
                    "(nombre, apellidos, especialidad) "
                    "VALUES "
                    f"('{profesor['nombre']}', "
                    f"'{profesor['apellidos']}', "
                    f"'{profesor['especialidad']}');\n"
                )
                f.write(consulta)

        print("Archivo import.sql creado correctamente")

