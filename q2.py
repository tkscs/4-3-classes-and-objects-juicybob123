class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()
class dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says woof!")

niki = dog("niki")
niki.speak()