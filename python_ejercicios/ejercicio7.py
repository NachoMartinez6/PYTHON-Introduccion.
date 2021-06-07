        ### FOR ###

## FOR - string

# cadena = input("Ingrese una palabra: ")
# print(cadena)
# print(type(cadena))
# print(len(cadena))

# for caracter in cadena:
#     print(caracter)


## FOR - lista

# cadena = ["Python", "Ingles", "Máster", "Carnet"]

# for cachito in cadena:
#     print("---" + cachito + "---")
#     for caracter in cachito:
#         caracter = caracter.lower()
#         if caracter in"aeoáéó":
#             print (caracter)
        

## FOR - por indices

# frutas = ["Mora", "Fresa", "Sandia", "Piña", "Uva"]
# precioxlb = [0.50, 1.00, 1.55, 1.20, 2.00]


# print("---Lista de fruta con precio menor a 1.50 libras ---")

# for i in range(len(frutas)):
#     fruta = frutas[i]
#     precio = precioxlb[i]
#     if precio < 1.50:
#         print(fruta,"-->", precio)




# frutas = ["Mora", "Fresa", "Mora", "Piña", "Uva"]
# cantidad = [5, 10, 3, 5, 10]
# clientes = ["Antonio", "Pablo", "Juan", "Emilio", "David"]

# for i in range(len(clientes)):
#     fruit = frutas[i]
#     quantity = cantidad[i]
#     customer = clientes [i]
#     if fruit == "Mora":
#         print("Cantidad comprada",quantity, "por", customer)

cadena = "JOSE IGNACIO"

for i in range(len(cadena)):
    caracter = cadena[i]
    print("posición", i, "-->", caracter)
    