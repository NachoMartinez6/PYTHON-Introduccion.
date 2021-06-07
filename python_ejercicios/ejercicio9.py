### WHILE ###


# x = (input("--> "))


# while not x.isdigit():
#     print("Por favor, ingrese correctamene")
#     x = (input("-->"))

# print("Programa terminado")

# i = 1

# while i <= 100:
#     print(i)
#     i += 1

# print("Programm is over")

# num = input("Write a number: ")

# while not num.isdigit():
#     print("Por favor, escribe un número")
#     num = input("Write a number: ")

# print("Fin del programa")


# cadena = input("Write a text: ")

# while not cadena.isalnum():
#     print("Por favor, escribe un texto")
#     cadena = input("Write a text: ")

# print("Fin del programa")





# num = int(input("Cuantos numeros desea ingresar: "))

# cont = 0
# acum = 0

# while cont < num:
#     x = int(input("Ingrese un numero: "))
#     acum += x
#     cont += 1

# print("El resultado acumulado es: ", acum)

message = " "
while message != "3":
    print("Bienvenido a tu calculadora")
    print("1. -SUMA")
    print("2. -RESTA")
    print("3. -SALIR")
    message = (input("Ingrese opción: "))
    if message == "1":
        x1 = int(input("Write a number: "))
        x2 = int(input("Write a number: "))
        resultado = x1 + x2
        print("Resultado: ", resultado)
    elif message == "2":
        x1 = int(input("Write a number: "))
        x2 = int(input("Write a number: "))
        resultado = x1 - x2
        print("Resultado: ",resultado)
    elif message == "3":
        print("Fin del programa")
    else:
        print("Inserte una opción valida")