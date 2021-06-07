
# PRIMER EJERCICIO
# Escribe la siguiente expresion algoritmica en una función

# (a**3 *(b**2 - 2*a*c) / 2*b)

print("CONGRATULATIONS!! Welcome to the first math program to solve algorithmic expressions")

a = float(input("Write the variable a --> "))
b = float(input("Write the variable b --> "))
c = float (input ("Write the variable c -->"))

# Primera función: para resolver el algoritmo

def add(a, b, c):
    return (a**3 * (b**2 - 2*a*c))/ (2*b)
    
resultado = add(a,b,c)

# Segunda función: para mostrar el resultado y los comentarios en funcion de su valor

def results(x):
    print(f"Your result is: {resultado}")

    if resultado > 0:
        print("Well done, you have good numbers")

    elif resultado == 0:
        print("You must increase your income")

    else:
        print("Be careful, you are in red numbers")

results(resultado)


# Prueba - Ciclo Infinito: para continuar resolviendo expresiones o no


while True:
    print("Ingresa (1) para continuar resolviendo algoritmos")
    print("Ingresa (2) para detener el programa")
    message = float(input("-->"))
    
    if message == 1:
        print("Gracias, añada nuevos valores a la expresión")
        a = float(input("Write the variable a --> "))
        b = float(input("Write the variable b --> "))
        c = float (input ("Write the variable c -->"))

        resultado = add(a, b, c)
        results (resultado)

    elif message == 2:
        print("Muchas gracias por usar nuestro programa. Hasta la próxima")
        break









