# This function performs the calculation based on input numbers and operation type
def calculate(first_number, second_number, operation_type):
    if operation_type == '/':
        if second_number == 0:
            return "Division by zero is not allowed"
        else:
            return first_number / second_number
    elif operation_type == "+":
        return first_number + second_number
    elif operation_type == "-":
        return first_number - second_number
    elif operation_type == "*":
        return first_number * second_number
    else:
        return "Invalid operation type"


def main():
    try:
        # Get the first number from the user
        first_number = float(input("Enter the first number: "))
        
        # Get the operation type from the user
        operation_type = input("Enter your operation type ('/','*','-','+'): ")
        
        # Get the second number from the user
        second_number = float(input("Enter the second number: "))

        # Call the calculate function with the input values and print the result
        result = calculate(first_number, second_number, operation_type)
        print("Result:", result)

    except ValueError:
        # Handle the case where the user enters invalid input (non-numeric)
        print("Invalid input. Please enter valid numerical values.")
    except ZeroDivisionError:
        # Handle the case where division by zero occurs
        print("Cannot divide by zero!")
    except Exception as e:
        # Handle any other unexpected errors
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()