
from unittest.mock import patch
import unittest
from src.views.calculator_view import CalculatorView
from src.utils.output_formatting import format_result
from src.operations.addition import add
from src.operations.subtraction import subtract
from src.operations.multiplication import multiply
from src.operations.division import divide
from src.operations.modulo import modulo
from src.operations.exponentiation import exponentiate

class TestCalculatorView(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '+'])
    def test_get_user_input(self, mock_input):
        calculator_view = CalculatorView()
        result = calculator_view.get_user_input()
        self.assertEqual(result, ['1', '2', '+'])

    @patch('builtins.input', side_effect=['1', '2', '+'])
    def test_perform_operation(self, mock_input):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['1', '2', '+'])
    def test_display_result(self, mock_input):
        calculator_view = CalculatorView()
        with patch('builtins.print') as mock_print:
            calculator_view.display_result(3)
            mock_print.assert_called_once_with(format_result(3))

    def test_addition(self):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation(1, 2, add)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation(1, 2, subtract)
        self.assertEqual(result, -1)

    def test_multiplication(self):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation(1, 2, multiply)
        self.assertEqual(result, 2)

    def test_division(self):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation(1, 2, divide)
        self.assertEqual(result, 0.5)

    def test_modulo(self):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation(1, 2, modulo)
        self.assertEqual(result, 1)

    def test_exponentiation(self):
        calculator_view = CalculatorView()
        result = calculator_view.perform_operation(1, 2, exponentiate)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
