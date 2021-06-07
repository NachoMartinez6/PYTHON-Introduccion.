        ### JUEGO DE 'CHO HAN' ###

import random as rd

billetera = 10
acum = 0
message ="si"


print("---Bienvenido a CHO HAN---")
print(f"Usted tiene {billetera} libras en la billetera")
while billetera > 0 and message == "si":
    apuesta = int(input("Ingrese apuesta: "))
    if 0 < apuesta <= billetera:
        dado1 = rd.randint(1,6)
        dado2 = rd.randint(1,6)
        total = dado1 +dado2
        resto = total%2
        parimpar = input("Adivina ¿par o impar? ".lower())
        print("Salió: {} + {} = {}".format(dado1,dado2,total))
        if resto == 0 and parimpar == "par":
            print("!Ganó¡")
            billetera += apuesta
            acum += 1
            print(f"Usted tiene: {billetera}")
        elif resto != 0 and parimpar == "impar":
            print("!Ganó¡")
            billetera += apuesta
            acum += 1
            print(f"Usted tiene: {billetera}")
        elif resto== 0 and parimpar == "impar":
            print("!Perdió¡")
            billetera -=apuesta
            print(f"Usted tiene: {billetera}")
        elif resto != 0 and parimpar == "par":
            print("!Perdió¡")
            billetera -= apuesta
            print(f"Usted tiene: {billetera}")
        if billetera != 0:
            message = input("¿Desea continuar (si) o (no)? ").lower()
            print("------------------------------")
        if billetera == 0:
            print("No te queda dinero en la billetera")
    elif apuesta > billetera:
        print("No tiene tanto dinero en la billetera")
    elif apuesta <= 0:
        print("Ingrese una apuesta valida")

print("Gracias por jugar")
print(f"Usted gano: {acum} partida(s)")