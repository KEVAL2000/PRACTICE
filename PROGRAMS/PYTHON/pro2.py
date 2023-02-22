#Inheritance
#Create class
class Quadrilateral:
    #Create constructor
    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
    #Create method
    def perimeter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print("Perimeter: ", p)
#Create object and instantiate class
q = Quadrilateral(4,5,6,7)
#Call class method
q.perimeter()

#Create child class of Parent class
class Rectangle(Quadrilateral):
    #Create constructor and add parent constructor
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
#Create object and instantiate class
r = Rectangle(4,2)
#Call parent class method
r.perimeter()