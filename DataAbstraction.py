class Employee:
    salary = 50000
    __company = "Kod Factory" # Data Abstraction using __ before variable name

    def printEmpDetails(self):
        # print(self.id)
        print(self.salary)
        print(Employee.__company)


obj = Employee()

# obj.id=20
setattr(obj, "id", 20)

# print(obj.ids)

# print(getattr(obj, "ids", 0))

# To check if given attribute is available in class or not
print(hasattr(obj, "id"))

delattr(obj, 'id')

# print(obj.id)
print(hasattr(obj, "id"))
# print(obj.id)
# obj.printEmpDetails()

print("aditya's new bike")