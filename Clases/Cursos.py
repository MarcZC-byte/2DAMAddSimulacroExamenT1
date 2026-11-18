import xml.etree.ElementTree as ET

from conexion.conexion_bd import ConexionBD


class Cursos:

    def __init__(self):
        self.curso_id = None
        self.nombre = None
        self.duracion_horas = None
        self.precio = None

    def leerCursos(self):
        cursos = []
        with open("./archivos/cursos.xml", "r", encoding="utf-8") as f:
            arbol = ET.parse(f)
            raiz = arbol.getroot()

        for curso in raiz:
            datos = {}
            print(curso.tag)
            for dato in curso:
                print(f" {dato.tag}: {dato.text}")
                if dato.tag != "curso_id":
                    datos[dato.tag] = dato.text

            cursos.append(datos)
        return cursos

    def insertarCursos(self):
        consulta = (
            "INSERT INTO curso (nombre,duracion_horas,precio)"
            "VALUES (%s,%s,%s)"
        )

        cursos = self.leerCursos()

        with ConexionBD() as cnx:
            cursor = cnx.cursor()

            for curso in cursos:
                valores = (
                    curso["nombre"],
                    curso["duracion_horas"],
                    curso["precio"]
                )

                cursor.execute(consulta, valores)

            cnx.commit()
            cursor.close()

        print(f"Cursos procesados: {len(cursos)}")

