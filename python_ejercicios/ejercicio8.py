
# actividades = ["Inglés", "Deporte", "Coche", "Inglés"]
# tiempos_hora = [4, 1.5, 1, 2.5]
# personas = ["Nacho", "Samu", "Rafa", "Paula"]

# for i in range(len(actividades)):
#     actividad = actividades[i]
#     tiempo_hora = tiempos_hora[i]  
#     if tiempo_hora <= 1.5:
#         print(actividad, tiempo_hora)
    

# for i in range(len(personas)):
#     actividad = (actividades[i])
#     tiempo_hora = (tiempos_hora[i])
#     persona = (personas[i])
#     if actividad == "Inglés":
#         print("---Lista de actividad---")
#         print(actividad)
#         print(tiempo_hora, "horas")
#         print(persona)


## EJERCICIO 2.3 PIOGRAM

# a = int(input("Ingrese numero: "))
# resto = a%2
# condicion=resto ==0

# print(condicion)









### EJERCICIO 9.4 PIOGRAM


# i = int(input("Cuantos numeros desea ingresar: "))
# cont = 0
# suma = 0

# for numero in range(i):
#     print("--- Ciclo " + str(numero+1) + " ---")
#     numero = int(input("Ingrese numero: "))
#     if numero%2 == 0:
#         cont += 1
#     else:
#         suma = suma + numero
        
# print("Contador de numeros pares: " + str(cont))
# print("Suma de numeros impares: " + str(suma))




# x = int(input("Cuantos numeros va a ingresar: "))
# cont = 0
# acum = 0

# for numero in range(x):
#     print("Ciclo - " + str(numero+1))
#     numero = int(input("Ingrese numero: "))
#     if numero%2 == 0:
#         cont += 1
#     else: 
#         acum += numero

# print(cont, acum)


friends_list = ["Jv", "edu", "pablo", "juan", "rafa"]
train_horas = [2, 0, 2, 0, 1]

# for i in friends_list:
#     print(i)

# for i in range(len(friends_list)):
#     friend = friends_list[i]
#     hora = train_horas[i]
#     if hora > 0:
#         print("Amigo: ", friend, " entrena ", hora, " h por día")
#     else:
#         print("Amigo: ", friend, " (No entrena)")