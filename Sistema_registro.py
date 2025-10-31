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
elif opcion == 4:
        pago = 3000
        deportes = "Alberca, Tenis y Padel"
    else:
        print("Opcion no valida, inteta de nuevo. \n")
    continue

cont_personas += 1
ingreso_total += pago
suma_pagos += pago
resumen_clientes += "Nombre: " + nombre + " | Deportes: " + deportes + " | Pago: $" + str(pago) + "\n"

print()
print("REPORTE FINAL - CLUB BRITANIA")
print("\n")
print("Total de socios registrados:", cont_personas)
print("\nresumen de clientes:\n")

print("\nResumen de clientes:\n")
print(resumen_clientes)

print()
print("Total por deporte:")
print("Alberca:", cont_alberca, "personas | Ingreso: $", ingresos_alberca)
print("Tenis:", cont_tenis, "personas | Ingreso: $", ingresos_tenis)
print("Padel:", cont_padel, "personas | Ingreso: $", ingresos_padel)

print()
print("Ganancia total: $", ingreso_total)

if cont_personas > 0:
    print("Promedio de ganancia por persona: $", ingreso_total / cont_personas)

print("\nRegistro finalizado con éxito.")









