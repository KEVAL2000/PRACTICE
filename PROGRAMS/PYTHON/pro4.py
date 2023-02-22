#Encapsulation
#Create class
class Student:
    #Create constructor
    def __init__(self, a, b, c):
        self.name = a
        #Use Protected modifier
        self._department = b
        #Use Private modifier
        self.__year = c
    def show(self):
        print("Year: ", self.__year)

student = Student("KEVAL", "IT", 2000)

print("Name: ", student.name)
print("Department: ", student._department)
#Use name mangling to access private member
print("Year: ", student._Student__year)
#Call class method
student.show()