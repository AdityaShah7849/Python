# Class : Group of objects

class Employee:
    age = 25
    dept = 'Sales'
    # Class member function must have 1st parameter as self
    def printName(self, name):
        print("Hello",name)
        print("Your age is",self.age)


obj = Employee()
obj1 = Employee()

obj.age = 40
obj1.age = 50

obj.printName("Adi")
obj1.printName("Jayesh")

# print(obj.age)
# print(obj.dept)