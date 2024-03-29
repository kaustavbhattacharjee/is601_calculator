import unittest,csv
from decimal import *
from Calculator.Calculator import Calculator
from CsvReader.my_csv_reader import read_csv

class MyTestCase(unittest.TestCase):
    calculator = Calculator()  #common object for all the test methods


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator,Calculator)

    def test_add(self):
        test_row_list = read_csv("addition.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=self.calculator.add(a,b)
            self.assertEqual(exp_result,c)

    def test_subtract(self):
        test_row_list = read_csv("subtraction.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=self.calculator.subtract(a,b)
            self.assertEqual(exp_result,c)

    def test_multiply(self):
        test_row_list = read_csv("multiplication.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=self.calculator.multiply(a,b)
            self.assertEqual(exp_result,c)

    def test_divide(self):
        test_row_list = read_csv("division.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=float(row[2])
            exp_result=self.calculator.divide(a,b)
            self.assertEqual(exp_result,c)

    def test_square(self):
        test_row_list = read_csv("square.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            #c=int(row[2])
            exp_result=self.calculator.square(a)
            self.assertEqual(exp_result,b)

    def test_square_root(self):
        test_row_list = read_csv("square_root.csv")
        for row in test_row_list:
            a=int(row[0])
            b=Decimal(row[1])
            #c=float(row[2])
            exp_result=self.calculator.square_root(a)
            self.assertEqual(exp_result,b)

if __name__ == '__main__':
    unittest.main()