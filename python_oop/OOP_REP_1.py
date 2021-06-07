## REPASO CLASE OOP

# class Amigos:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#         print("-FRIEND CREATED-")
#         print("-------------")
#     def upgrade_name (self, new_name):
#         self.name = new_name
#         print("Nombre updated")
#         print("-------------")
#     def upgrade_age(self, new_age):
#         self.edad = new_age
#         print("Age updated")
#         print("-------------")




# a1 = Amigos("Juan", 24)
# print(a1.nombre, a1.edad)

# a1.upgrade_name("Juanxo")
# print(a1.name, a1.edad)

# a2 = Amigos("Rafa", 24)
# print(a2.nombre, a2.edad)

# a2.upgrade_age(27)
# print(a2.nombre, a2.edad)



# amigos = [Amigos("Nacho", 24), 
# Amigos("Edu", 25), 
# Amigos("Emilio", 22)]

# print(amigos[0].nombre, amigos[0].edad, amigos[1].nombre, amigos[1].edad, amigos[2].nombre)




# class Proyectos:
#     def __init__(self, name_proyect, actual_state):
#         self.name_proyect = name_proyect
#         self.actual_state = actual_state
#         print("--- New proyect created ---")
#         # print(name_proyect, actual_state)
#     def upgrade_name(self, new_name):
#         self.name_proyect = new_name
#         print("(Name Successfully Updated)")
#     def upgrade_state(self, new_state):
#         self.actual_state = new_state
#         print("(State Successfully Updated)")
#     def __str__(self):
#         return self.name_proyect + (" ") + self.actual_state
#     def print_all_proyects (proyectos):
#         for i in range(len(proyectos)):
#             proyecto = p_act[i]
#             print(i + 1, proyecto)

# # p1 = Proyectos("Ingles: ", "B2 (ACTUALMENTE)")
# # p2 = Proyectos("Python: ", "OOP - (ACTUALMENTE)")

# # p2.upgrade_name("German")
# # p2.upgrade_state("Not yet")


# p_act =[Proyectos("Ingles: ", "B2 (ACTUALMENTE)"),
# Proyectos("Python: ", "OOP - (ACTUALMENTE)"),
# Proyectos("Genera: ", "NOT YET"),
# Proyectos("German: ", "NOT YET")]


# print(p_act[0], p_act[1])

# Proyectos.print_all_proyects(p_act)









### REPASO EJERCICIO GETTER Y SETTER

class Customer:
    def __init__(self, name, age, wallet):
        self.__name = name
        self.__age = age
        self.__wallet = wallet
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, valor):
        self.__name = valor

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valor):
        self.__age = valor

    @property
    def wallet(self):
        return self.__wallet

    @wallet.setter
    def wallet(self, valor):
        self.__wallet = valor

    def __str__(self):
        return "Name: " + self.__name + ", Age: " + str(self.__age) + ", Wallet: " + str(self.wallet)
    
    def print_all_customers(customers):
        for i in range(len(customers)):
            customer = customers[i]
            print(i+1, customer)
    Hash = None
    __repr__ = __str__

# c1 = Customer("Juan", 24, 1000)
# c2 = Customer("Nacho", 24, 200)
# c3 = Customer("Edu", 25, 1452)

customers = [Customer("Juan", 24, 1000),
Customer("Nacho", 24, 200),
Customer("Edu", 25, 1452)]

# print(c1)
# print(c2)
# print(c3)

# print(customers[0].name)

# Customer.print_all_customers(customers)
print(customers)





