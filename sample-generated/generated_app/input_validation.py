
def validate_numeric_input(input_string):
  """
  Validates if the input string represents a valid numeric value.

  Args:
      input_string: The string to validate.

  Returns:
      True if the input string is a valid numeric value, False otherwise.
  """
  try:
    float(input_string)
    return True
  except ValueError:
    return False

def validate_operation(operation):
  """
  Validates if the input operation is supported.

  Args:
      operation: The operation symbol to validate.

  Returns:
      True if the operation is supported, False otherwise.
  """
  supported_operations = ["+", "-", "*", "/", "%", "^"]
  return operation in supported_operations

