CAPACIDAD = 50

vehiculos = {}

vehiculos_atendidos = 0
recaudacion_total = 0
total_horas = 0

def ingresar_vehiculo():

    if len(vehiculos) >= CAPACIDAD:
        print("Error: no hay lugares disponibles.")
        return

    patente = input("Ingrese la patente: ")

    if patente in vehiculos:
        print("Error: el vehículo ya se encuentra estacionado.")
        return

    hora_ingreso = int(input("Ingrese la hora de ingreso (0-23): "))

    if hora_ingreso < 0 or hora_ingreso > 23:
        print("Error: hora inválida.")
        return

    vehiculos[patente] = hora_ingreso

    print("Vehículo registrado correctamente.")


def registrar_egreso():

    global vehiculos_atendidos
    global recaudacion_total
    global total_horas

    patente = input("Ingrese la patente: ")

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
