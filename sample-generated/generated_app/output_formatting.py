
def format_result(operation, num1, num2, result):
    """Formats the output of the calculator based on the operation performed.

    Args:
        operation (str): The operation performed.
        num1 (float): The first operand.
        num2 (float): The second operand.
        result (float): The result of the operation.

    Returns:
        str: The formatted output string.
    """
    if operation == "+":
        return f"{num1} + {num2} = {result}"
    elif operation == "-":
        return f"{num1} - {num2} = {result}"
    elif operation == "*":
        return f"{num1} * {num2} = {result}"
    elif operation == "/":
        return f"{num1} / {num2} = {result}"
    elif operation == "%":
        return f"{num1} % {num2} = {result}"
    elif operation == "**":
        return f"{num1} ** {num2} = {result}"
    else:
        return "Invalid operation!"
