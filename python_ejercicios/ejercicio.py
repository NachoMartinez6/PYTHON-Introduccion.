#### PRIMER EJERCICIO - CONDICIONALES ####

# message = " "
# cont = 0

# while message != "no":
#     numero = int(input("Write a number: "))
#     if numero > 0: 
#         print("numero is a positive number")
#         cont += 1
#     elif numero == 0:
#         print("numero is 0")
#         cont += 1
#     else:
#         print("numero is a negative number")
#         cont += 1
#     message = input("¿Quiere continuar con el programa 'si' o 'no'?: ").lower()
#     print("--------------------------")

# print("Has realizado: ", cont, "operación(es)")
# print("---Fin del programa---")

######## SEGUNDO EJERCIRIO - FUNCIONES ############

message_1 = " "
cont = 0
acum = 0

while not message_1 == "2":
    a = float(input("Valor a --> "))
    b = float(input("Valor b --> "))
    c = float(input("Valor c --> "))
    resultado = (a**3 *(b**2 - 2*a*c))/(2*b)
    
    if resultado < 0:
        print ("El numero es negativo")
        print(f"Resultado: {resultado}")
        cont += 1
        acum += resultado
    elif resultado > 0:
        print("El numero es positivo")
        print(f"Resultado: {resultado}")
        cont += 1
        acum += resultado
    else:
        print("El numero es 0")
        print(f"Resultado: {resultado}")
        cont += 1
        acum += resultado
    message_1 = input("Quieres continuar con el programa (1) o terminar (2): ").lower()

print("El numero de operaciones totales fue: ", cont)
print("La suma total fue: ", acum)


print("Fin del programa")





