#   SISTEMA DE REGISTRO - CLUB BRITANIA

import time

def mostrar_carga():
    print("CARGANDO PROGRAMA")
    for i in range(10): #Esta linea de codigo indica cuantas veces se va a imprimir "."
        print(".", end="", flush=True) #El print "." puede ser modificado, por ejemplo le puedes poner "-" y se va a imprimir una linea horizontal del mismo
        time.sleep(0.3) #Esta funcion es cuando el programa se va a apagar y encender
    print(" Listo!\n")


mostrar_carga()

# Función: guardar los cliente en los archivos

def guardar_en_archivo(cliente):
    try:
        with open("registro_britania.txt", "a") as archivo:
            archivo.write("Nombre: " + cliente["nombre"] +
                          " | Deporte: " + cliente["deporte"] +
                          " | Pago: $" + str(cliente["pago"]) + "\n")
    except:
        print("Error al guardar en archivo.")

#Funcion: Registrar cliente

def registrar_cliente (estadisticas,clientes):
    nombre = input ("Nombre del socio (o escribe cancelar ):")

    if nombre.lower() == "cancelar" or "Cancelar":
#   SISTEMA DE REGISTRO - CLUB BRITANIA

import time

def mostrar_carga():
    print("CARGANDO PROGRAMA")
    for i in range(10): #Esta linea de codigo indica cuantas veces se va a imprimir "."
        print(".", end="", flush=True) #El print "." puede ser modificado, por ejemplo le puedes poner "-" y se va a imprimir una linea horizontal del mismo
        time.sleep(0.3) #Esta funcion es cuando el programa se va a apagar y encender
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

    if nombre.lower() == "cancelar" or "Cancelar":
        print("Registro cancelado.\n")
        return None

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
        estadisticas["ingreso_padel"] += pago

    elif opcion == 4:
        deporte = "Alberca, Tenis y Padel"
        pago = 3000

        # Cuenta una persona en cada deporte
        estadisticas["cont_alberca"] += 1
        estadisticas["cont_tenis"] += 1
        estadisticas["cont_padel"] += 1

        # Repartimos el pago de memberesia completa entre los 3 deportes
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
    print()
    print("        Reporte final - Club britania    ")
    print()

    print("Total de socios registrados:", len(clientes))
    print("\nResumen de clientes:\n")

    for c in clientes:
        print("Nombre:", c["nombre"], "| Deporte:", c["deporte"], "| Pago: $", c["pago"])

    print("\nTotal por deporte:")
    print("Alberca:", estadisticas["cont_alberca"], "personas | Ingreso: $", estadisticas["ingreso_alberca"])
    print("Tenis:", estadisticas["cont_tenis"], "personas | Ingreso: $", estadisticas["ingreso_tenis"])
    print("Padel:", estadisticas["cont_padel"], "personas | Ingreso: $", estadisticas["ingreso_padel"])

    print("\nGanancia total: $", estadisticas["ingreso_total"])

    if len(clientes) > 0:
        print("Promedio por persona: $", estadisticas["ingreso_total"] / len(clientes))

    print("\nLos datos también fueron guardados correctamente")
    print()
    
# Menu con funcion while

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
    print("========= MENÚ PRINCIPAL =========")
    print("1. Registrar socio")
    print("2. Ver reporte")
    print("3. Salir")
    print("===================================")

    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        registrar_cliente(estadisticas, clientes)

    elif opcion == "2":
        mostrar_reporte(estadisticas, clientes)

    elif opcion == "3":
        print("Saliendo del sistema... ¡Gracias por usarlo!")
        break

    else:
        print("Opción incorrecta. Intenta de nuevo.\n")












