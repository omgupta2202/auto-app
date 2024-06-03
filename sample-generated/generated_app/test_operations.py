
from calculator.src.operations.addition import add
from calculator.src.operations.subtraction import subtract
from calculator.src.operations.multiplication import multiply
from calculator.src.operations.division import divide
from calculator.src.operations.modulo import modulo
from calculator.src.operations.exponentiation import exponentiate

import unittest

class TestOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 0), 0)

    def test_division(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-6, 3), -2)
        self.assertRaises(ZeroDivisionError, divide, 6, 0)

    def test_modulo(self):
        self.assertEqual(modulo(7, 3), 1)
        self.assertEqual(modulo(-7, 3), -1)
        self.assertEqual(modulo(0, 5), 0)

    def test_exponentiation(self):
        self.assertEqual(exponentiate(2, 3), 8)
        self.assertEqual(exponentiate(-2, 3), -8)
        self.assertEqual(exponentiate(2, 0), 1)

if __name__ == '__main__':
    unittest.main()
