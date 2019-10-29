import unittest,csv
from Calculator import Calculator

class MyTestCase(unittest.TestCase):


    def test_instantiate_calculator(self):
        calculator=Calculator()
        self.assertIsInstance(calculator,Calculator)

    def test_add(self):
        calculator = Calculator()
        test_add_file_path = "./src/addition.csv"
        csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
        next(csv_reader)
        test_add_row_list=list()
        for row in csv_reader:
            test_add_row_list.append(row)
        for row in test_add_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=calculator.add(a,b)
            self.assertEqual(exp_result,c)

    def test_subtract(self):
        calculator = Calculator()
        test_add_file_path = "./src/subtraction.csv"
        csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
        next(csv_reader)
        test_add_row_list=list()
        for row in csv_reader:
            test_add_row_list.append(row)
        for row in test_add_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=calculator.subtract(a,b)
            self.assertEqual(exp_result,c)

    def test_multiply(self):
        calculator = Calculator()
        test_add_file_path = "./src/multiplication.csv"
        csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
        next(csv_reader)
        test_add_row_list=list()
        for row in csv_reader:
            test_add_row_list.append(row)
        for row in test_add_row_list:
            a=int(row[0])
            b=int(row[1])
            c=int(row[2])
            exp_result=calculator.multiply(a,b)
            self.assertEqual(exp_result,c)

    def test_divide(self):
        calculator = Calculator()
        test_add_file_path = "./src/division.csv"
        csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
        next(csv_reader)
        test_add_row_list=list()
        for row in csv_reader:
            test_add_row_list.append(row)
        for row in test_add_row_list:
            a=int(row[0])
            b=int(row[1])
            c=float(row[2])
            exp_result=calculator.divide(a,b)
            self.assertEqual(exp_result,c)

    def test_square(self):
        calculator = Calculator()
        test_add_file_path = "./src/square.csv"
        csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
        next(csv_reader)
        test_add_row_list=list()
        for row in csv_reader:
            test_add_row_list.append(row)
        for row in test_add_row_list:
            a=int(row[0])
            b=int(row[1])
            #c=int(row[2])
            exp_result=calculator.square(a)
            self.assertEqual(exp_result,b)

if __name__ == '__main__':
    unittest.main()