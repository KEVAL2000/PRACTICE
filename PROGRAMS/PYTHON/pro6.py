#Method overloading
from multipledispatch import dispatch

@dispatch(int, int)
def product(a,b):
    p = a*b
    print(p)

@dispatch(int, int, int)
def product(a, b, c):
    p = a*b*c
    print(p)

@dispatch(float, float, float)
def product(a, b, c):
    p = a*b*c
    print(p)

product(2, 3)
product(2, 3 ,4)
product(2.2, 3.2, 4.2)