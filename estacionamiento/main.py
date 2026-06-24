from funciones import *

opcion = 0

while opcion != 6:

    print("\n===== ESTACIONAMIENTO =====")
    print("1. Ingresar vehículo")
    print("2. Registrar egreso")
    print("3. Ver vehículos estacionados")
    print("4. Ver espacios disponibles")
    print("5. Ver estadísticas")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        ingresar_vehiculo()

    elif opcion == 2:
        registrar_egreso()

    elif opcion == 3:
        mostrar_estacionados()

    elif opcion == 4:
        mostrar_disponibles()

    elif opcion == 5:
        mostrar_estadisticas()

    elif opcion == 6:
        print("Programa finalizado.")

    else:
        print("Opción inválida.")
