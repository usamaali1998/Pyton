#Inheritance = Allows a class to inherit attributes and methods from class
# Helps with code reusability and extensiability
# class Child()parent

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mouse(Animal):
    def speak(self):
        print("queek")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
