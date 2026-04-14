class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{sefl.name} says meow!")

ella = Cat("Ella")
ella.speak()