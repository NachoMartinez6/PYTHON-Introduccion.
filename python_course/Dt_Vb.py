                    #### DATATYPES ####


# STRINGS - textos 

# No es lo mismo Hello World que Hello world
# Ojo a como escribimos el codigo
print("hello world")
print('hello world')
print('''hello world''')
print("""hello world""")

print(type("hello world"))
#La funcion + puede usarse para concatenar textos
print("bye"+"world")

#NÚMEROS

#INTEGER - numeros enteros
print(30)
print(type(30))

#FLOAT - numeros decimales (flotantes)
print(type(30.5))

#BOOLEAN - Estados
print(type(True))
print(type(False))

#List - listas de numeros y/o textos
print(type([10,20,30,55]))
print(type(["hello","bye","world"]))
print(type([10,"bye",True,10.1]))
print(type([]))

#Tuples o tupla - Listas inmutables
print(type((10,20,55)))
print(type(()))
print((20,"hello"))

#Diccionarios o diccionaries
print({"Name": "JOSÉ IGNACIO",
"Surenames": "MARTÍNEZ PÉREZ",
"Nickname": "NACHO"
})

print({"lat":121,
"lon":56
})

print(type({"lat":121,
"lon":56
}))


#None - No esta definido aun por un tipo de dato
None

#Variables

mi_nombre = "Nacho"
print(mi_nombre)







                        #### VARIABLES ####


# Definir una variable

name = "JOSÉ IGNACIO"
surname ="MARTÍNEZ PÉREZ"

print(name)
print(name, surname)

x = 100

#Case sensitive 
Book = "Crea hábitos"
book = "Crea hábitos"

_2book = "Crea hábitos"

x = 100
book = "I robot"

#Escribir variables seguidas
print(x)
print(book)

#Escribir variables de seguido
x, book = 100, "I robot"
print(x, book)

#CONVENCIONES
book_name = "I robot"
bookName = "Ironman"
BookName = "I am"

#Constantes
PI = 3.1416
print(PI)

#Python es un lenguaje dinámico
#Reasignar variables unicamente reescribiendo el valor de la variable

book_name = "I robot"
book_name = "I am"

print(book_name)