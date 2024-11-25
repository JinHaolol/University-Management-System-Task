class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def makeNoise(self):
        print("Meow")
    
    def play(self, cat):
        print(self.name + " is playing with " + cat.name)

    def fight(self, dog):
        print(self.name + " is fighting " + dog.name)

class Dog(Cat):
    def __init__ (self,name,colour,breed):
    super().__init__(self,name,colour,)
    self.breed = breed

    def makeNoise(self):
        print("woof")

    def stateBreed(self):
        print(self.name, " is a " , self.breed)

import math

class Shape:
    def __init__(self,1side,2side):
        self.1side = 1side
        self.2side = 2side

    def caculate_area():
       return int(2side) * int(1side)
    
class Circle(Shape):
    def __init__(self,1radius):
    super().__init__(self, 1radius)
    self.1radius = 1radius

    def caculte_area():
        return int(1radius)**2 * 3.141592654
    
class Triangle(Shape):
    def __init__(self,1side,2side):

    def caculate_area():
        return 0.5 * int(1side) * int(2side)
    