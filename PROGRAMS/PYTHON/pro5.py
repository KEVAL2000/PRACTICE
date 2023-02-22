#Abstraction
#Create abstract class
from abc import ABC, abstractmethod
class Polygon(ABC):
    #Create abstract method
    @abstractmethod
    def sides(self):
        print("Abstract method")
class Triangle(Polygon):
    def sides(self):
        #Call abstract method using super()
        super().sides()
        print("Triangle has 3 sides")
class Square(Polygon):
    def sides(self):
        print("Square has 4 sides")
class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")
class Hexagone(Polygon):
    def sides(self):
        print("Hexagone has 6 sides")

t = Triangle()
t.sides()
s = Square()
s.sides()
p = Pentagon()
p.sides()
h = Hexagone()
h.sides()