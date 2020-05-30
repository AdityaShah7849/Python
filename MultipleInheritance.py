# Multiple Inheritance

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

class Crocodial(LandAnimal, SeaAnimal):
    def dangerous(self):
        print("Very dangerous...")

obj = Crocodial()

obj.dangerous()
obj.swim()
obj.walk