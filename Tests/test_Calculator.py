import unittest,csv
from decimal import *
from Calculator.Calculator import Calculator

def read_csv(path):
    test_add_file_path = path
    csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
    next(csv_reader)
    test_row_list = list()
    for row in csv_reader:
        test_row_list.append(row)
    return test_row_list

class MyTestCase(unittest.TestCase):
    calculator = Calculator()  #common object for all the test methods


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator,Calculator)

    def test_add(self):
        test_row_list = read_csv("/Tests/Data/addition.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=self.calculator.add(a,b)
            self.assertEqual(exp_result,c)

    def test_subtract(self):
        test_row_list = read_csv("/Tests/Data/subtraction.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=self.calculator.subtract(a,b)
            self.assertEqual(exp_result,c)

    def test_multiply(self):
        test_row_list = read_csv("/Tests/Data/multiplication.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=self.calculator.multiply(a,b)
            self.assertEqual(exp_result,c)

    def test_divide(self):
        test_row_list = read_csv("/Tests/Data/division.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            c=float(row[2])
            exp_result=self.calculator.divide(a,b)
            self.assertEqual(exp_result,c)

    def test_square(self):
        test_row_list = read_csv("/Tests/Data/square.csv")
        for row in test_row_list:
            a=int(row[0])
            b=int(row[1])
            #c=int(row[2])
            exp_result=self.calculator.square(a)
            self.assertEqual(exp_result,b)

    def test_square_root(self):
        test_row_list = read_csv("/Tests/Data/square_root.csv")
        for row in test_row_list:
            a=int(row[0])
            b=Decimal(row[1])
            #c=float(row[2])
            exp_result=self.calculator.square_root(a)
            self.assertEqual(exp_result,b)

if __name__ == '__main__':
    unittest.main()