from math import sqrt

def add (n1, n2):
    x = (n1 + n2)
    print(f"El resultado es {x}")


def ec_sg (a, b, c):
    if (b**2 -(4*a*c)) >= 0:
        x1 = (-b + sqrt(b**2 - (4*a*c)))/ (2*b) 
        x2 = (-b - sqrt(b**2 - (4*a*c)))/ (2*b)
        print(f"Los resultados son {x1} y {x2}")
    
    else:
        print("La solucion es con numeros complejos")

