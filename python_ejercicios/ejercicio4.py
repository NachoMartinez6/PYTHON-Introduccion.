
# print("Bienvenido al programa HealthyChange, aquí te monstraremos las métricas adecuadas y consejos")

# peso = int(input("Por favor, indiquenos su peso en Kg: "))
# estatura = int(input("Por favor, indiquenos su altura en centímetros: "))


# imc = (peso/ estatura**2)

# print(imc)


def f_imc (peso, estatura):
    imc = peso/ (estatura/100)**2
    print(f"El resultado de su indice es {imc}")
    if imc >=25:
        print("Seria recomendable dieta rica en verduras y actividad fisica de al menos media hora")
    if 18 <= imc <25:
        print ("Esta usted en un muy buen peso para su edad, mantenga rutinas y hábitos saludables")
    if imc <18:
        print(" Seria aconsejable que aumentase la ingesta calórica diaría con alimentos saludables")


# f_imc(peso, estatura)

