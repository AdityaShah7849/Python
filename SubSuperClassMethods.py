class LandAnimal:
    def walk(self):
        print("walking...")

class SeaAnimal:
    def swim(self):
        print("Swimming...")

class Dog(LandAnimal):
    def bark(self):
        print("Barking...")

class Fish(SeaAnimal):
    def die(self):
        print("Die outside water...")

obj = Dog()
obj1 =Fish()

# print(issubclass(Dog, LandAnimal))
# print(issubclass(Dog, SeaAnimal))

# print(isinstance(obj, Dog))
# print(isinstance(obj1, Dog))
