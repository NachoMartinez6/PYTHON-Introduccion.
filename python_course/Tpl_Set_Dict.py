#### TUPLES ####



x = (1, 2, 3)
print(type(x))
print(x)

y = ("January", "Febreary","March")
print(y)

numeros = tuple((1, 2, 3))
print(numeros)
print(type(numeros))

# print(dir(x))

z = (1,)
print(type(z))

print(x[0])

# del x 
# print(x)

locations = {(35.5, 95.5): "Tokyo",
(45.5, 62.2): "New york"
}
print(locations)






                #### SETS ####

colors = {"red", "green", "blue"}
print(type(colors))

print(colors)

# No puedo seleccionar segun el indice porque no tiene
# print(colors[2])

# Añadir colores
colors.add("violet")
print(colors)

colors.remove("red")
print(colors)

# colors.clear()
# print(colors)

# del colors
# print (colors)





                #### DICTIONARIES ####

product = {"name": "book",
"quantity": 5,
"price": 4.99
}

person = {"first_name": "Ryan",
"last_name": "ray"}

print(type(product))

# print(dir(person))

# print(product.keys())
# print(product.values())
print(product.items())

# del product

# product.clear()
# print(product)

products = [
{"name": "book", "quantity": 35},
{"name": "laptop", "quantity": 14}
]

print(products)