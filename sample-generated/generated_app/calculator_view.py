
from src.operations.addition import add
from src.operations.subtraction import subtract
from src.operations.multiplication import multiply
from src.operations.division import divide
from src.operations.modulo import modulo
from src.operations.exponentiation import exponentiate
from src.utils.input_validation import validate_input
from src.utils.output_formatting import format_result

def calculator_view():
    """
    Presents the user with the calculator interface, handles user input and performs calculations.
    """

    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Exponentiation")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting Calculator...")
            break

        if not validate_input(choice, '1', '7'):
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        if not validate_input(num1) or not validate_input(num2):
            print("Invalid input. Please enter valid numbers.")
            continue

        num1 = float(num1)
        num2 = float(num2)

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = modulo(num1, num2)
        elif choice == '6':
            result = exponentiate(num1, num2)

        print(f"Result: {format_result(result)}")

if __name__ == "__main__":
    calculator_view()

