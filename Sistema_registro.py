import time

def mostrar_carga():
    print()
    print("Cargando programa\n")
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(" Listo!\n")

mostrar_carga()

# Función: guardar cliente en archivo
def guardar_en_archivo(cliente):
    try:
        with open("registro_britania.txt", "a") as archivo:
            archivo.write("Nombre: " + cliente["nombre"] +
                          " | Deporte: " + cliente["deporte"] +
                          " | Pago: $" + str(cliente["pago"]) + "\n")
    except:
        print("Error al guardar en archivo.")

# Función: registrar cliente
def registrar_cliente(estadisticas, clientes):
    nombre = input("Nombre del socio (o escribe cancelar): ")

    # Validación para nombre vacío
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.\n")
        return None

    # Cancelar finaliza todo el programa 
    if nombre.lower() == "cancelar":
        print("\nRegistro cancelado por el usuario.")
        print("Saliendo del sistema... ¡Hasta luego!\n")
        return "SALIR"

    print("¿Qué deporte realiza?")
    print("1. Alberca")
    print("2. Tenis")
    print("3. Padel")
    print("4. Más de un deporte (Membresía completa)")

    try:
        opcion = int(input("Elige una opción (1-4): "))
    except:
        print("Error: debes ingresar un número.\n")
        return None

    if opcion == 1:
        deporte = "Alberca"
        pago = 1800
        estadisticas["cont_alberca"] += 1
        estadisticas["ingreso_alberca"] += pago

    elif opcion == 2:
        deporte = "Tenis"
        pago = 2350
        estadisticas["cont_tenis"] += 1
        estadisticas["ingreso_tenis"] += pago

    elif opcion == 3:
        deporte = "Padel"
        pago = 2400
        estadisticas["cont_padel"] += 1
        estadisticas["ngreso_padel"] += pago

    elif opcion == 4:
        deporte = "Alberca, Tenis y Padel"
        pago = 3000

        estadisticas["cont_alberca"] += 1
        estadisticas["cont_tenis"] += 1
        estadisticas["cont_padel"] += 1

        estadisticas["ingreso_alberca"] += 1000
        estadisticas["ingreso_tenis"] += 1000
        estadisticas["ingreso_padel"] += 1000

    else:
        print("Opción no válida.\n")
        return None

    cliente = {
        "nombre": nombre,
        "deporte": deporte,
        "pago": pago
    }

    clientes.append(cliente)
    estadisticas["ingreso_total"] += pago
    guardar_en_archivo(cliente)

    print("Registro exitoso.\n")
    return cliente

# Función: mostrar reporte
def mostrar_reporte(estadisticas, clientes):
    print("\n====================================")
    print("   Reporte final - Club Britania      ")
    print("====================================\n")

    print("Total de socios registrados:", len(clientes))
    print("\nResumen de clientes:\n")

    for datos in clientes:
        print("Nombre:", datos["nombre"], "| Deporte:", datos["deporte"], "| Pago: $", datos["pago"])

    print("\nTotal por deporte:")
    print("Alberca:", estadisticas["cont_alberca"], "personas | Ingreso: $", estadisticas["ingreso_alberca"])
    print("Tenis:", estadisticas["cont_tenis"], "personas | Ingreso: $", estadisticas["ingreso_tenis"])
    print("Padel:", estadisticas["cont_padel"], "personas | Ingreso: $", estadisticas["ingreso_padel"])

    print("\nGanancia total: $", estadisticas["ingreso_total"])

    if len(clientes) > 0:
        print("Promedio por persona: $", estadisticas["ingreso_total"] / len(clientes))

    print("\nLos datos fueron guardados correctamente\n")

# Menú con While True
clientes = []

estadisticas = {
    "cont_alberca": 0,
    "cont_tenis": 0,
    "cont_padel": 0,
    "ingreso_alberca": 0,
    "ingreso_tenis": 0,
    "ingreso_padel": 0,
    "ingreso_total": 0
}

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Registrar socio")
    print("2. Ver reporte")
    print("3. Salir")
    print("====================================\n")

    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        resultado = registrar_cliente(estadisticas, clientes)
        if resultado == "SALIR":
            break

    elif opcion == "2":
        mostrar_reporte(estadisticas, clientes)

    elif opcion == "3":
        print("Saliendo del sistema... ¡Gracias por usarlo!")
        break

    else:
        print("Opción incorrecta. Intenta de nuevo.\n")






















