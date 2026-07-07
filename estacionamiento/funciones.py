import datetime

CAPACIDAD = 50

vehiculos = {}

vehiculos_atendidos = 0
recaudacion_total = 0
total_horas = 0


def guardar_datos():

    archivo = open("datos.txt", "w")

    archivo.write(str(vehiculos_atendidos) + "\n")
    archivo.write(str(recaudacion_total) + "\n")
    archivo.write(str(total_horas) + "\n")

    for patente in vehiculos:
        archivo.write(patente + ";" + str(vehiculos[patente]) + "\n")

    archivo.close()


def cargar_datos():

    global vehiculos
    global vehiculos_atendidos
    global recaudacion_total
    global total_horas

    try:

        archivo = open("datos.txt", "r")

        vehiculos_atendidos = int(archivo.readline())
        recaudacion_total = int(archivo.readline())
        total_horas = int(archivo.readline())

        vehiculos = {}

        for linea in archivo:
            datos = linea.strip().split(";")
            patente = datos[0]
            hora = int(datos[1])
            vehiculos[patente] = hora

        archivo.close()

    except FileNotFoundError:

        vehiculos = {}
        vehiculos_atendidos = 0
        recaudacion_total = 0
        total_horas = 0


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
        print("Error: el vehículo ya se encuentra estacionado.")
        return

    hora_ingreso = int(input("Ingrese la hora de ingreso (0-23): "))

    if hora_ingreso < 0 or hora_ingreso > 23:
        print("Error: hora inválida.")
        return

    vehiculos[patente] = hora_ingreso

    print("Vehículo registrado correctamente.")

    registrar_en_log(f"INGRESO - Patente: {patente} | Hora indicada: {hora_ingreso}:00 hs")

    guardar_datos()


def registrar_egreso():

    global vehiculos_atendidos
    global recaudacion_total
    global total_horas

    patente = input("Ingrese la patente: ").upper()

    if patente not in vehiculos:
        print("Error: vehículo no encontrado.")
        return

    hora_salida = int(input("Ingrese la hora de salida (0-23): "))

    if hora_salida < 0 or hora_salida > 23:
        print("Error: hora inválida.")
        return

    hora_ingreso = vehiculos[patente]

    if hora_salida < hora_ingreso:
        print("Error: la hora de salida no puede ser menor que la de ingreso.")
        return

    horas = hora_salida - hora_ingreso

    importe = horas * 1000

    print("Horas de permanencia:", horas)
    print("Importe a pagar: $", importe)

    vehiculos_atendidos += 1
    recaudacion_total += importe
    total_horas += horas

    del vehiculos[patente]

    print("Egreso registrado correctamente.")

    registrar_en_log(f"EGRESO - Patente: {patente} | Permanencia: {horas} hs | Cobrado: ${importe}")

    guardar_datos()


def mostrar_estacionados():

    if len(vehiculos) == 0:
        print("No hay vehículos estacionados.")
        return

    print("\nVehículos estacionados:")

    for patente in vehiculos:
        print(patente)


def mostrar_disponibles():

    ocupados = len(vehiculos)

    disponibles = CAPACIDAD - ocupados

    print("\nCapacidad total:", CAPACIDAD)
    print("Lugares ocupados:", ocupados)
    print("Lugares disponibles:", disponibles)


def mostrar_estadisticas():

    print("\n===== ESTADÍSTICAS =====")

    print("Vehículos atendidos:", vehiculos_atendidos)
    print("Recaudación total: $", recaudacion_total)

    if vehiculos_atendidos > 0:

        promedio = total_horas / vehiculos_atendidos

        print("Tiempo promedio de permanencia:", promedio, "horas")

    else:

        print("Todavía no se registraron egresos.")
