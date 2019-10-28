import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator=Calculator()
        self.assertIsInstance(calculator,Calculator)

    def test_results_property_calculator(self):
        calculator=Calculator()
        self.assertEqual(calculator.result,3)

    def test_calculator_add(self):
        calculator=Calculator()
        self.assertEqual(calculator.add(3,4),7)
if __name__ == '__main__':
    unittest.main()