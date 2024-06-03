
def divide(a, b):
  """
  Divides two numbers.

  Args:
      a (float): The dividend.
      b (float): The divisor.

  Returns:
      float: The quotient of a divided by b.

  Raises:
      ZeroDivisionError: If b is zero.
  """
  if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")
  return a / b
