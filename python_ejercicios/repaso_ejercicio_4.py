
# Crear un diccionario (datos - cliente)

print("Bienvenido al programa IMC V2.0. para calcular tu IMC")

name = input("Cual es tu nombre: ")
surname = input ("Cual es tu apellido: ")

print (f"Muy buenas {name}")

print("Ingrese datos para analisis")

# age = float(input("Cual es tu edad: "))
estatura = int(input("Cual es tu estatura (cm):"))
peso = float(input("Cual es tu peso (Kg): "))

#Importamos la función para realizar el analisis de masa corporal

from ejercicio4 import f_imc

f_imc(peso, estatura)

for i in range(2):
    print(" ")

print("---Tabla IMC---")

for i in range(2):
    print(" ")
import pandas as pd 

df = pd.read_excel("C:\\Users\\Nacho\\Desktop\\PYTHON\\tabla_imc.xlsx")

print(df)