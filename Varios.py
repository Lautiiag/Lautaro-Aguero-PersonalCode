"varios"
import csv
import os








def main():
    while True:
        try:
            print("1. Cargar herramientas")
            print("2. Mostrar herramientas registradas")
            print("3. Modificar herramienta")
            print("4. Eliminar herramienta")
            print("5. Consultar disponibilidad")
            print("6. Listar productos sin stock")
            print("7. Salir")

            opt=input("Ingrese opcion")
            match opt:              
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    break
                case _:
                    print("no hay opt")
        except ValueError:
            print("Error: Se esperaba número entero.")
if __name__ == "__main__":
    main()
