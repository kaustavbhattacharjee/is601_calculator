from Calculator.Def_Files.Addition import addition
from Calculator.Def_Files.Subtraction import subtraction
from Calculator.Def_Files.Multiplication import multiplication
from Calculator.Def_Files.Division import division
from Calculator.Def_Files.Square import squaring
from Calculator.Def_Files.SquareRoot import square_rooting

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