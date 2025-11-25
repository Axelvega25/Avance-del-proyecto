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
