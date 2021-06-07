######### TERCER EJERCICIO - FUNCIONES ###########

from math import sqrt

# a = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
# b = float(input("Escribe el valor del coeficiente de la variable lineal: "))
# c = float(input("Escribe el valor independiente: "))

# if (b**2-(4*a*c))>=0:
#     x1 = (-b + sqrt(b**2 - (4*a*c))) /(2*a)
#     x2 = (-b - sqrt(b**2 - (4*a*c))) /(2*a)
#     print(f"los dos resultados son {x1} y {x2}")
# else:
#     print("La solucion es con numeros complejos")

print("Programa ECSG V 2.0 para realizar ecuaciones de segundo grado")

def add(A, B, C):
    if (B**2-(4*A*C))>=0:
        x1 = (-B + sqrt(B**2 - (4*A*C))) /(2*A)
        x2 = (-B - sqrt(B**2 - (4*A*C))) /(2*A)
        print(f"Los dos resultados son {x1} y {x2}")
    else:
        print("La solución es con números complejos")

A = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
B = float(input("Escribe el valor del coeficiente de la variable lineal: "))
C = float(input("Escribe el valor independiente: "))

add(A, B, C)


# A = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
# B = float(input("Escribe el valor del coeficiente de la variable lineal: "))
# C = float(input("Escribe el valor independiente: "))




# info_message = input("Quieres resolver otra ecuacion de segundo grado: ")
# while info_message == ("Si") or ("SI"):
#     A = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
#     B = float(input("Escribe el valor del coeficiente de la variable lineal: "))
#     C = float(input("Escribe el valor independiente: "))
#     add(A, B, C)
#     info_message = input("Quieres resolver otra ecuacion de segundo grado: ")
# else: print("Muchas gracias. Hasta la proxima")





# def info_message(respuesta="Muchas gracias. ¡Hasta pronto!"):
#     message = input("¿Quieres resolver otra ecuación de segundo grado?: ")
#     while message == ("Si") or ("SI"):
#         A = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
#         B = float(input("Escribe el valor del coeficiente de la variable lineal: "))
#         C = float(input("Escribe el valor independiente: "))
#         add(A, B, C)
#         def info_message(respuesta)
#     else: print("Muchas gracias. !Hasta pronto¡")







# info_message = input("¿Quieres resolver otra ecuación de segundo grado?: ")
# if info_message == ("Si") or ("si"):
#     A = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
#     B = float(input("Escribe el valor del coeficiente de la variable lineal: "))
#     C = float(input("Escribe el valor independiente: "))
#     add(A, B, C)
#     info_message = input("¿Quieres resolver otra ecuación de segundo grado?: ")
#     if info_message == ("Si") or ("si"):
#         A = float(input("Escribe el valor del coeficiente de la variable cuadrática: "))
#         B = float(input("Escribe el valor del coeficiente de la variable lineal: "))
#         C = float(input("Escribe el valor independiente: "))
#         add(A, B, C)
#         print("Muchas gracias. ¡Hasta la próxima!")
#     else:print("Muchas gracias. ¡Hasta la próxima!")
# else: 
#     print("Muchas gracias. ¡Hasta la próxima!")


