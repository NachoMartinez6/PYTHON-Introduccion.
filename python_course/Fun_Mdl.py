
            #### FUNCTIONS ####


# print("dsa")
# print(dir("sad"))
# print(type(3))

# def hi():
#     print("Hello world")

# hi()

# def hello(name="everyone"):
#     print("Hello " + name + " welcome back to You Talk TV")
#     print("You are the number ", 1)
    
   

# hello("Nacho")
# hello("Laura")
# hello("Victor")
# hello("Salva")
# hello()

def add(n1, n2):
    return n1 + n2

print(add(10, 30))

def add2 (number_one, number_two):
    return number_one * number_two

print (add(12, 12))
print(add2(600, 10))


add = lambda N1, N2:  N1 * N2

print(add (25, 25))


                #### MODULES ####

            
### MODULOS ###

## MODULO DE PYTHON ##

# MODULO DATETIME

# from datetime import timedelta, date

# print(date.today())
# print(timedelta(minutes=100))


## MI PROPIO MODULO ##

# MODULO FMATH

# 1º Importar modulo entero

# import fmath

# fmath.add(100,25)
# fmath.ec_sg(1, 4, 4)

# 2º Importar las funciones que vaya a utilizar

# from fmath import add, ec_sg

# add(100, 25)
# ec_sg(1, 4, 4)
  
  
## MODULO DE TERCEROS - PIP MODULES  ##

# MODULO COLORAMA

# from colorama import init, Fore, Style, Back


# init(convert = True)


# print(Fore.BLUE + "Hello world")
# print (Back.WHITE + "Hello world")

# print (Style.BRIGHT + "Hello world") #BRILLANTE
# print (Style.DIM + "Hello world") #OSCURA
# print (Style.NORMAL + "Hello world") #NORMAL

# print (Style.RESET_ALL)

## MODULO TERMCOLOR Y COLORAMA

from colorama import init
from termcolor import colored 

init (convert = True)
print(colored("Hello world", "red", "on_white"))


# print (Style.RESET_ALL)

print("Hello world")