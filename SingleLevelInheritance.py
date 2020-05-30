# Single level and Multilevel Inheritance

class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class ChildDog(Dog):
    def crying(self):
        print("Crying...")

# obj = Dog()

# obj.bark()
# obj.eat()

obj1 = ChildDog()

obj1.eat()
obj1.bark()
obj1.crying()