import datetime
import os

CAPACIDAD = 50

vehiculos = {}
estadisticas = {}


def guardar_datos():

    with open("vehiculos.txt", "w", encoding="utf-8") as archivo:

        for patente in vehiculos:

            ingreso = vehiculos[patente].strftime("%Y-%m-%d %H:%M:%S")

            archivo.write(patente + ";" + ingreso + "\n")

    with open("estadisticas.txt", "w", encoding="utf-8") as archivo:

        for fecha in estadisticas:

            datos = estadisticas[fecha]

            archivo.write(
                fecha + ";" +
                str(datos["vehiculos"]) + ";" +
                str(datos["recaudacion"]) + ";" +
                str(datos["horas"]) + "\n"
            )


def cargar_datos():

    global vehiculos
    global estadisticas

    vehiculos = {}
    estadisticas = {}

    if os.path.exists("vehiculos.txt"):

        with open("vehiculos.txt", "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split(";")

                patente = datos[0]

                ingreso = datetime.datetime.strptime(
                    datos[1],
                    "%Y-%m-%d %H:%M:%S"
                )

                vehiculos[patente] = ingreso

    if os.path.exists("estadisticas.txt"):

        with open("estadisticas.txt", "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split(";")

                estadisticas[datos[0]] = {
                    "vehiculos": int(datos[1]),
                    "recaudacion": float(datos[2]),
                    "horas": float(datos[3])
                }


def registrar_en_log(mensaje):

    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("registro_estacionamiento.txt", "a", encoding="utf-8") as archivo:

        archivo.write(f"[{ahora}] {mensaje}\n")


def ingresar_vehiculo():

    if len(vehiculos) >= CAPACIDAD:
        print("Error: no hay lugares disponibles.")
        return

    patente = input("Ingrese la patente: ").upper()

    if patente in vehiculos:
        print("Error: el vehículo ya está estacionado.")
        return

    ingreso = datetime.datetime.now()

    vehiculos[patente] = ingreso

    print("Vehículo registrado correctamente.")
    print("Fecha y hora de ingreso:", ingreso.strftime("%d/%m/%Y %H:%M:%S"))

    registrar_en_log(
        f"INGRESO - Patente: {patente} | {ingreso.strftime('%d/%m/%Y %H:%M:%S')}"
    )

    guardar_datos()


def registrar_egreso():

    patente = input("Ingrese la patente: ").upper()

    if patente not in vehiculos:
        print("Error: vehículo no encontrado.")
        return

    ingreso = vehiculos[patente]

    salida = datetime.datetime.now()

    horas = (salida - ingreso).total_seconds() / 3600

    if horas < 1:
        horas = 1

    importe = round(horas * 1000, 2)

    fecha = salida.strftime("%d/%m/%Y")

    if fecha not in estadisticas:

        estadisticas[fecha] = {
            "vehiculos": 0,
            "recaudacion": 0,
            "horas": 0
        }

    estadisticas[fecha]["vehiculos"] += 1
    estadisticas[fecha]["recaudacion"] += importe
    estadisticas[fecha]["horas"] += horas

    del vehiculos[patente]

    print("Tiempo de permanencia:", round(horas, 2), "horas")
    print("Importe a pagar: $", importe)

    registrar_en_log(
        f"EGRESO - Patente: {patente} | {round(horas,2)} hs | ${importe}"
    )

    guardar_datos()


def mostrar_estacionados():

    if len(vehiculos) == 0:
        print("No hay vehículos estacionados.")
        return

    print("\nVehículos estacionados:\n")

    for patente in vehiculos:

        print(
            patente,
            "- Ingresó:",
            vehiculos[patente].strftime("%d/%m/%Y %H:%M:%S")
        )


def mostrar_disponibles():

    print("\nCapacidad total:", CAPACIDAD)
    print("Lugares ocupados:", len(vehiculos))
    print("Lugares disponibles:", CAPACIDAD - len(vehiculos))


def mostrar_estadisticas():

    if len(estadisticas) == 0:

        print("Todavía no hay estadísticas.")
        return

    print("\n===== ESTADÍSTICAS POR DÍA =====\n")

    for fecha in sorted(estadisticas):

        datos = estadisticas[fecha]

        promedio = datos["horas"] / datos["vehiculos"]

        print("Fecha:", fecha)
        print("Vehículos atendidos:", datos["vehiculos"])
        print("Recaudación: $", round(datos["recaudacion"], 2))
        print("Promedio de permanencia:", round(promedio, 2), "horas")
        print("--------------------------------")
