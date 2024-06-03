
from calculator.exceptions.zero_division_error import ZeroDivisionError

def divide(num1, num2):
    """
    Performs division of two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2
