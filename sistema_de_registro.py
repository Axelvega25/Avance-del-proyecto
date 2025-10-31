num_clientes = int(input("Cuántos clientes se registrarán: "))

ingresos_totales = 0
suma_edades = 0
contador_clientes = 0

basica_client = 0 
premium_client = 0
vip_client = 0

cliente_mas_joven = 999
cliente_mayor = 0 
nombre_mas_joven = ""
nombre_mayor = ""

resumen_clientes = ""

while contador_clientes < num_clientes:
    nombre = input("\nNombre del cliente (o escribe 'cancelar' para salir): ")

    if nombre == "cancelar" or nombre == "Cancelar":
        print("Registro cancelado.\n")
        break

    edad = int(input("Edad: "))
    membresia = input("Tipo de membresia (Basica, Premium, Vip): ")
    tipo_de_persona = input("Tipo de persona (Estudiante, Profesor, Ninguno): ")

    if edad < 18 and (membresia != "Basica" and membresia != "basica"):
        print("Solo se permite membresia basica para menores. Intenta de nuevo.")
        continue

    if edad < 18:
        tarifa = 200
    elif edad <= 40:
        if membresia == "Basica" or membresia == "basica":
            tarifa = 300 
        elif membresia == "Premium" or membresia == "premium":
            tarifa = 500
        else:
            tarifa = 700
    elif edad <= 59:
        if membresia == "Basica" or membresia == "basica":
            tarifa = 250
        elif membresia == "Premium" or membresia == "premium":
            tarifa = 450
        else:
            tarifa = 600
    else:
        if membresia == "Basica" or membresia == "basica":
            tarifa = 300
        elif membresia == "Premium" or membresia == "premium":
            tarifa = 500
        else:
            tarifa = 700
        tarifa = tarifa - (tarifa * 0.20)

    if tipo_de_persona == "Estudiante" or tipo_de_persona == "estudiante":
        tarifa = tarifa - (tarifa * 0.15)  
    elif tipo_de_persona == "Profesor" or tipo_de_persona == "profesor":
        tarifa = tarifa - (tarifa * 0.10)                            

    ingresos_totales += tarifa
    suma_edades += edad
    contador_clientes += 1

    if membresia == "Basica" or membresia == "basica":  
        basica_client += 1
        membresia_guardada = "Basica"
    elif membresia == "Premium" or membresia == "premium":
        premium_client += 1
        membresia_guardada = "Premium"
    else:
        vip_client += 1
        membresia_guardada = "Vip"

    if edad < cliente_mas_joven:
        cliente_mas_joven = edad
        nombre_mas_joven = nombre

    if edad > cliente_mayor:
        cliente_mayor = edad
        nombre_mayor = nombre

    resumen_clientes += "Nombre: " + nombre + " | Edad: " + str(edad) + " | Membresia: " + membresia_guardada +  " | Pago: $" + str(tarifa) + "\n"  

if contador_clientes > 0:
    promedio_edad = suma_edades / contador_clientes
else:
    promedio_edad = 0

print()
print("Reporte final - Gimnasio")
print()
print("Total de clientes registrados:", contador_clientes)
print("\nResumen de clientes:")
print(resumen_clientes)
print()
print("Total de ingresos: $", ingresos_totales)
print("Promedio de edad:", promedio_edad)
print("Clientes por membresia - Basica:", basica_client, " Premium:", premium_client, " Vip:", vip_client)
print("Cliente mas joven:", nombre_mas_joven, "con", cliente_mas_joven, "años")
print("Cliente de mayor edad:", nombre_mayor, "con", cliente_mayor, "años")
print()

