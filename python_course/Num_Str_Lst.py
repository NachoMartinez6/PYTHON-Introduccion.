                #### NÚMEROS ####


print(type(10))
print(type(10.5))

# Usuario - Inserte un valor en la consola
age = input("Insert your age: ")
print(age)
print(type(age))

# Como lo ha escrito el usuario esta en 'str'
# Convertimos a int con funcion int()
new_age = (int(age)+ 5)
print(new_age)






                #### STRINGS ####


myStr = "Hello world"
print(myStr)
nombre = "Nacho"
print(nombre)

# dir(myStr)

# # COMENTA EL CODIGO - NO EJECUTE
# # print(dir(myStr))

# # Para cambiar mismos caracteres (May. - Min.)
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())

# #Para reemplazar caracteres o palabras por otras
# print(myStr.replace("Hello", "bye"))
# print(myStr.replace("Hello", "bye").upper())

# # Para contar carácteres
# print(myStr.count(" "))

# # Para saber si empieza o termina por uno o varios caracteres
# print(myStr.startswith("Hello"))
# print(myStr.endswith("world"))

# # Para separar mi string
# print(myStr.split())

# # Para encontrar la posicion de una letra
# print(myStr.find("o"))

print("my name is " + nombre)
print(f"my name is {nombre}")






                #### LISTS ####

# Para crear listas usamos snake_case
demo_list = [1, "HELLO", 1.2, True, [1,2,3]]
colours_list = ["red", "green", "blue"]
numbers_list = [1, 2 , 3, 4]
print(type(numbers_list))


print(numbers_list, colours_list)

# Para crear listas de rangos
r = list(range(1,11))
print(r)

# print(dir(list))

# Para conocer la longitud de la lista
print(len(demo_list))

#Para conocer la posición de un elemento
print(colours_list[0])


# Para conocer si hay un objeto concreto dentro de la lista
print("green" in colours_list)
# print(4 in r)

# Para cambiar un dato de la lista
colours_list[1] = "yellow"
print(colours_list)

# print(dir(colours_list))

# Para añadir valores a la lista 

# colours_list.append("violet")
# colours_list.extend(["violet","green"])
colours_list.extend(("pink","black"))
print(colours_list)
# print(len(colours_list))

# En una posición concreta
# colours_list.insert(1, "violet")
colours_list.insert(len(colours_list), "violet")
print(colours_list)


# # Para eliminar valores de la lista
# colours_list.pop()
# print(colours_list)
# colours_list.remove("blue")
# print(colours_list)

# colours_list.clear()
# print(colours_list)
