import csv
from dataclasses import fields

from mysql.connector import cursor

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

    def buscarAlumno(self, n:str):
        consulta = (
            "SELECT nia, nombre, apellidos, email, fecha_nacimiento FROM alumno "
            "WHERE nia = %s"
        )
        resultado= []
        with ConexionBD() as cnx:
            cursor = cnx.cursor()
            cursor.execute(consulta, (n,))
            for  nia, nombre, apellidos, email, fecha_nacimiento in cursor:
                print("Nia: " + str(nia) + ", Nombre:" + nombre + ",Apellidos: " +apellidos + ", Email: " + email + ", Fecha nacimiento: "+ str(fecha_nacimiento))
                resultado.append("Nia: " + str(nia) + ", Nombre: " + str(nombre) + ", Apellidos: " +str(apellidos) + ", Email: " + str(email) + ", Fecha nacimiento: "+ str(fecha_nacimiento))
            cursor.close()
        return resultado

    def modificar_alumno(self, n: str):
        consulta = (
            "UPDATE alumno SET nombre = %s, apellidos = %s, "
            "email = %s, fecha_nacimiento = %s "
            "WHERE nia = %s"
        )
        nombre = input("Introduce el nuevo nombre: ")
        apellidos = input("Introduce los nuevos apellidos: ")
        email = input("Introduce el nuevo email: ")
        fecha_nacimiento = input("Introduce la nueva fecha de nacimiento (YYYY-MM-DD): ")

        with ConexionBD() as cnx:
            cursor = cnx.cursor()
            cursor.execute(consulta, (
                nombre,
                apellidos,
                email,
                fecha_nacimiento,
                n
            ))

            cnx.commit()

            if cursor.rowcount > 0:
                print("Alumno modificado correctamente")
            else:
                print("No se ha encontrado ningún alumno con ese NIA")

            cursor.close()

    def eliminar_alumno(self, n: str):
        consulta = (
            "DELETE FROM alumno WHERE nia = %s"
        )

        with ConexionBD() as cnx:
            cursor = cnx.cursor()
            cursor.execute(consulta, (n,))
            cnx.commit()
            if cursor.rowcount > 0:
                print("Alumno eliminado correctamente")
            else:
                print("No se ha encontrado ningún alumno con ese NIA")

            cursor.close()

