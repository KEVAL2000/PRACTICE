#Create class
class Car:
    #Create constructor
    def __init__(self, a, b, c):
        self.model = a
        self.year = b
        self.color = c
    #Create method
    def carDetail(self):
        print("Model: ",self.model)
        print("Year: ",self.year)
        print("Color: ",self.color)
#Create object and instantiate class
car1 = Car("Ford Mustang",2000,"Red")
#Call class method
car1.carDetail()