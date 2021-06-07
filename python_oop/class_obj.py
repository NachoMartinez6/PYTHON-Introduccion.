


# class Customer:
#     def __init__(self, name, membership_type):
#         self.name = name
#         self.membership_type = membership_type
#         print("Customer created")
#     def upgrade_membership(self, new_membership):
#         self.membership_type = new_membership
#     def upgrade_name(self, new_name):
#         self.name = new_name
  

# c1 = Customer("Juan", "Premium")


# c2 = Customer("Nacho", "Gold")

# # customers = [Customer("Caleb", "Gold"),
# # Customer("Brad", "Bronze")]

# print([customers[0].name, customers[0].membership_type],
# [customers[1].name, customers[1].membership_type])
# # Customer.read_customer()



# c = Customer("Caleb", "Gold")
# print(c.name, c.membership_type)

# c.upgrade_membership("Silver")
# print(c.name, c.membership_type)

# c.upgrade_name("Carlos")
# print(c.name, c.membership_type)



# print(customers[0].name, customers[1].membership_type)

# customers[0].upgrade_membership("Diamond")
# print(customers[0].name, customers[0].membership_type)











class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        # print("Customer created")
    def upgrade_membership(self, new_membership):
        self.membership_type = new_membership
    def upgrade_name(self, new_name):
        self.name = new_name
    def __str__(self):
        return self.name + (" ") + self.membership_type
    def print_all_customers(customers):
        for i in range(len(customers)):
            customer = customers[i]
            print(i+1, customer)
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
           return True
        else:
            return False
    __hash__ = None
    __repr__ = __str__ 


customers = [Customer("Caleb", "Gold"),
Customer("Brad", "Bronze"),
Customer("Caleb", "Gold"),
Customer("Nacho", "Premium")]



print(customers[0] == customers[2])


print(customers[0], customers[2])
print(id(customers[0]), id(customers[2]))

print(customers)








# c1 = Customer("Maria", "Gold")
# print(c1.name)
# print(customers[0], customers[1])


# # Customer.print_all_customers(customers)
# Customer.print_all_customers(customers)
