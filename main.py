
from Academia import  Academia

def main():
    academia = Academia()
    print("\nBIENVENIDO A LA GESTIÓN DE LA ACADEMIA")

    while True:
        
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cargar datos de cursos")
        print("2. Cargar datos de alumnos")
        print("3. Cargar datos de profesores")
        print("4. Cargar datos de matrículas")
        print("5. Mostrar todos los cursos")
        print("6. Mostrar todos los alumnos")
        print("7. Mostrar todas las matrículas")
        print("8. Buscar un alumno")
        print("9. Modificar datos de un alumno")
        print("10. Eliminar un alumno")
        print("11. Generar fichero import.sql")
        print("12. Salir")

        opcion = input("\nElige una opción: ")
        
        match opcion:
            case "1":
                academia.cargar_cursos()

            case "2":
                academia.cargar_alumnos()

            case "3":
                academia.cargar_profesores()

            case "4":
                academia.cargar_matriculas()

            case "5":
                academia.mostrar_cursos()

            case "6":
                academia.mostrar_alumnos()

            case "7":
                academia.mostrar_matriculas()

            case "8":
                academia.buscar_alumno()

            case "9":
                academia.modificar_alumno()

            case "10":
                academia.eliminar_alumno()

            case "11":
                academia.generar_import_sql()

            case "12":
                print("\nSaliendo del programa...")
                break

            case _:
                print("\nElige una opción válida")


if __name__ == '__main__':
    main()
