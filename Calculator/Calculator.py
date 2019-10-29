from decimal import *

def addition(a,b):
    return (a + b)

def subtraction(a,b):
    return (b - a)

def multiplication(a,b):
    return (a*b)

def division(a,b):
    return round(float(b/a),9)

def squaring(a):
    return (a**2)

def square_rooting(a):
    getcontext().prec = 10
    return (Decimal(a) ** Decimal(0.5))
class Calculator:

    def __init__(self):
        pass

    def add(self,a,b):
        return addition(a,b)

    def subtract(self,a,b):
        return subtraction(a,b)
    def multiply(self,a,b):
        return multiplication(a,b)
    def divide(self,a,b):
        return division(a,b)
    def square(self,a):
        return squaring(a)
    def square_root(self,a):
        return square_rooting(a)