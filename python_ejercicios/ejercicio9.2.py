
# REPASO JUEGO CHO HAN

import random as rd

message = (" ")
billetera = 10
acum = 0
cont = 0

print("Bienvenido a Cho Han")
print("Dispone de {}$ para apostar".format(billetera))

while message != "no" and billetera !=0:
    apuesta = int(input("¿Cuanto dinero quiere apostar? "))
    if 0 < apuesta <= billetera:
        dado1 = rd.randint(1, 6)
        dado2 = rd.randint(1, 6)
        resultado = dado1 + dado2
        resto = resultado%2
        parimpar = input("¿Eliga par o impar? ")
        print("El resultado es: {} + {} = {}".format(dado1, dado2, resultado))
        if parimpar== "par" and resto ==0:
            print("¡GANÓ!")
            billetera +=apuesta
            acum += 1
            cont += 1
        if parimpar == "impar" and resto != 0:
            print("¡GANÓ!")
            billetera += apuesta 
            acum += 1
            cont += 1
        if parimpar == "par" and resto != 0:
            print("¡PERDIÓ!")
            billetera -= apuesta
            cont += 1
        if parimpar == "impar" and resto == 0:
            print("¡PERDIÓ!")
            billetera -= apuesta
            cont += 1
    else:
        print("Ingrese una apuesta valida")

    print("Actualmente tiene {}$ en su billetera".format(billetera))
    if billetera > 0:
        message = input("¿Desea continuar jugando 'si' o 'no'? ")
        print("------------------------")
    
print(" ")
print("---RESUMEN---")
win_rate = (acum/cont)*100
print("Partida(s) ganada(s):{}".format(acum))
print("Partida(s) jugada(s)): {}".format(cont))
print("WinRate: {:.2f} %".format(win_rate))
print("Hasta la próxima")