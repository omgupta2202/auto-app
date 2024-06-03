
import unittest
from calculator.src.utils.input_validation import is_valid_number, is_valid_operation

class TestInputValidation(unittest.TestCase):

    def test_is_valid_number_valid_input(self):
        self.assertTrue(is_valid_number("123"))
        self.assertTrue(is_valid_number("0"))
        self.assertTrue(is_valid_number("-456.78"))
        self.assertTrue(is_valid_number("3.14159"))
        self.assertTrue(is_valid_number("1e6"))  # Scientific notation
        self.assertTrue(is_valid_number("1.2e-3"))  # Scientific notation

    def test_is_valid_number_invalid_input(self):
        self.assertFalse(is_valid_number("abc"))
        self.assertFalse(is_valid_number("123.4.5"))
        self.assertFalse(is_valid_number("123+456"))
        self.assertFalse(is_valid_number("123e"))
        self.assertFalse(is_valid_number("e123"))
        self.assertFalse(is_valid_number(" "))

    def test_is_valid_operation_valid_input(self):
        self.assertTrue(is_valid_operation("+"))
        self.assertTrue(is_valid_operation("-"))
        self.assertTrue(is_valid_operation("*"))
        self.assertTrue(is_valid_operation("/"))
        self.assertTrue(is_valid_operation("%"))
        self.assertTrue(is_valid_operation("**"))

    def test_is_valid_operation_invalid_input(self):
        self.assertFalse(is_valid_operation("a"))
        self.assertFalse(is_valid_operation("123"))
        self.assertFalse(is_valid_operation(" "))
        self.assertFalse(is_valid_operation("=="))
        self.assertFalse(is_valid_operation("!="))

if __name__ == '__main__':
    unittest.main()
