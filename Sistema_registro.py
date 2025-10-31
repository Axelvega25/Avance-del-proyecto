num_personas = int(input("¿Cuántas personas se registaran?:"))
cont_personas = 0
cont_alberca = 0
cont_tenis = 0
cont_padel = 0

ingresos_alberca = 0
ingresos_tenis = 0
ingresos_padel = 0
ingreso_total = 0

suma_pagos = 0
resumen_clientes = ""

while cont_personas < num_personas:
    nombre = input("Nombre del socio (o escribe cancelar para salir):")
    if nombre == "cancelar" or nombre == "Cancelar":
        print("Registro cancelado.\n")
        break
    print("Que deporte realiza?")
    print("1. Alberca")
    print("2. Tenis")
    print("3. Padel")
    print("4. Mas de un deporte (Membresia completa)")
    opcion = int(input("Elige una opcion (1-4): "))
if opcion == 1:
    pago = 1800
    cont_alberca += 1
    ingresos_alberca += pago
    deportes = "Alberca"
elif opcion == 2:
    pago = 2350
    cont_tenis += 1
    ingresos_tenis += pago
    deportes = "Tenis"
elif opcion == 3:
    pago = 2400
    cont_padel += 1
    ingresos_padel += pago
    deportes = "Padel"





