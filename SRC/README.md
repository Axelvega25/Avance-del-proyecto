Objetivo del proyecto:

El objetivo del proyecto es desarrollar un sistema en Python que permita registrar de manera sencilla el nombre de los socios, los deportes que practican y calcular automáticamente los ingresos por deporte, los totales y el promedio de ganancia por persona. Con esto, se pretende resolver el problema de control financiero y facilitar la operación diaria del Club Britania.

Roles de los integrantes:

Axel Antonio Vega Gonzalez (Senior)
Daniela Hernandez Sanchez (Mid)
Mariana Mendoza Alvidrez (Mid)
Aaron Fourzan Castillo (Junior) 
Pedro Antonio Rodriguez Grimaldo (Junior)

Instrucciones de instalación y ejecución:

En este sistema va a permitir registrar socios, validar sus datos, asignarles un deporte, calcular el pago correspondiente y generar un reporte completo del periodo.

----- Instalación

1. Descarga el archivo del programa (el que te proporcionaron o el que tengas guardado en tu computadora).

2. Asegúrate de tener Python 3.8 o superior instalado.

3. Guarda el archivo del sistema en una carpeta donde tengas permisos de lectura y escritura.

4. No necesitas instalar librerías externas; el programa funciona solo con herramientas básicas de Python.

----- Ejecución

1. Abre la carpeta donde guardaste el archivo.

2. Da doble clic si tu sistema lo permite, o bien:

Abre una terminal o consola.

Escribe:

python nombre_del_archivo.py

3. El sistema iniciará pidiendo cuántos socios deseas registrar.

4. Sigue las instrucciones en pantalla:

El flujo del funcionamiento del codigo

Escribe la cantidad de socios a registrar.

Ingresa el nombre de cada socio.

No se aceptan nombres vacíos.

Puedes escribir "cancelar" para detener todo el proceso inmediatamente.

----- Elige un deporte ingresando un número del 1 al 4:

1. Alberca


2. Tenis


3. Pádel


4. Membresía completa


----- Si el número es incorrecto, el sistema te avisará y repetirá el registro de ese socio.

----- El sistema va a calcula automáticamente el pago:

Alberca → $1800

Tenis → $2350

Pádel → $2400

Membresía completa → $3000


5. El sistema guardará todo en una lista interna con diccionarios, donde cada socio contiene:

“nombre”

“deporte”

“pago”


6. Cuando termine el registro, se generará un reporte final con:

Total de socios registrados.

Lista completa de socios con su deporte y pago.

Ingresos por cada deporte.

Ingreso total del periodo.

Promedio de ingreso por persona.

----- Recomendación de uso

Introduce bien los datos para evitar repeticiones.

Usa “cancelar” solo si realmente quieres detener todo el proceso.

Guarda los resultados si necesitas analizar los ingresos más tarde.
