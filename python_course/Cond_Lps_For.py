                #### CONDITIONALS ####

x = 15

if x >= 15:
    print("x is greater or equal than 15")
else: print("x is less than 15")

# print(3<2)
# print(x==15)

color = ("red")

if color == ("blue"):
    print("The color is blue")
elif color == ("red"):
    print("The color is red")
else: print("Any color")


name = ("John")
last_name = ("Snow")

if name == ("John"):
    if last_name == ("Carter"):
        print("You are John Carter")
    else: 
        print("You are not John Carter")
else: print("You are not John")

x=15

if x>2 and x<10: print ("x is less than 10 and more than 2")


if x>2 or x<=20: print("x is more than 2 or less or equal than 20")

y = 14

if (not x == y):
    print("x is not equal than y")



                #### LOOPS ####


foods = ["apple", "bread", "cheese", " milk", "bananas", "grapes"]
quantity =[15, 2, 0, 6, 0, 2]
# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])
# print(foods[4])

# for i in range(len(foods)):
#     food = foods[i]
#     if food == "cheese":
#         print("We need it --> ", food)
#     else:
#         print(food)


print("---Tabla de alimentos---")

# for i in range(len(foods)):
#     food = foods[i]
#     quant = quantity[i]
    
#     if 1< quant < 5:
#         print(quant, "-", food, "(replenish)")
#     if quant == 0:
#         print(quant, "-", food, "(default)")
#     if quant >=5:
#         print(quant, "-", food)
        


# for food in foods:
#     if food == "cheese":
#         continue
#     print(food)

# for numero in range (1, 8):
#     print(numero)

# for silaba in "Hello":
#     print(silaba)

# count = 4

# while count <= 10:
#     print(count)
#     count = (count + 1)



                    #### OPTIMIZACIÓN ####



# foods = ["apple", "bread", "cheese", "milk", "bananas", "grapes"]

# for i in range(len(foods)):
#     food = foods[i]
#     if food == "cheese":
#         print(food + "(reponer)")
#     else:
#         print(food)

for i in range (10):
    print(i+1,"COME SALUDABLE")

mystr = "Hello world"




for i in range(len(mystr)):
    letter = mystr[i]
    print(i+1, letter)



                #### FOR ####


# n = 5

# for name in range (n):
#     print("hola", name)

# for i in range(1,11):
#     print(i)

# for i in range(5,31,5):
#     print(i,"multiplo de 5")


# n = int(input("Escribe un numero: "))

for n in range(1,11):
    print("---Tabla " + str(n) + "---")
    for i in range(1,11):
        resultado = n * i
        print(n, "x", i, "=", resultado)


# while True:
#     print("1")
#     print("2")
#     message = int(input("--> "))
#     if message == 1:
#         print ("Ingrese nuevo valor")
#         f = int(input("--> "))
#         for e in range(1,11):
#             result = f * e
#             print(f, "x", e, "=", result)
#     if message == 2:
#         print("bye bye")
#         break