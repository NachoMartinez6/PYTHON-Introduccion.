# SEGUNDO EJERCICIO

# Definir la funcion para resolver la expresión algoritmica
#       x = (-b +- sqrt(b**2 - (4*a*c)))/ (2b)
# Realizar los condicionales necesarios para obtener todos los valores
# Definir una segunda funcion para realizar un bucle que permita resolver mas funciones o finalizar el programa

# Importar la funcion raiz cuadrada de la libreria math

from math import sqrt

# Añadir los valores que quiera para la funcion cuadratica

a = float(input("Escribe la componente cuadratica: "))
b = float (input("Escribe la componente lineal: "))
c = float (input("Escribe el valor independiente: "))

# Funcion para resolver ecuaciones de segundo grado

def add(a, b, c):
    if (b**2 -(4*a*c)) >= 0:
        x1 = (-b + sqrt(b**2 - (4*a*c)))/ (2*b) 
        x2 = (-b - sqrt(b**2 - (4*a*c)))/ (2*b)
        print(f"Los resultados son {x1} y {x2}")
    
    else:
        print("La solucion es con numeros complejos")

add(a, b, c)

# Ciclo infinito 

while True:
    print("Escribe (1) para continuar resolviendo ecuaciones de segundo grado")
    print("Escribe (2) para finalizar con el programa")
    message = float(input("-->"))
    if message == 1:
        print("Okey, añade los nuevos valores")
        a = float(input("Escribe la componente cuadratica: "))
        b = float (input("Escribe la componente lineal: "))
        c = float (input("Escribe el valor independiente: "))
        add (a, b, c)

    elif message == 2:
        print("Muchas gracias. Hasta pronto")
        break
    else:
        print("Muchas gracias. Hasta pronto")
        break
