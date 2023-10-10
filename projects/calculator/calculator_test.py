import unittest

from projects.calculator.calculator import Calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1,2), 3)

    def test_sum_negative(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(-15,5),-10)

if __name__ == '__main__':
    unittest.main()