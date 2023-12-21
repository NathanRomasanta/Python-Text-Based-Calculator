def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def calculator():
    print(logo)
    con = True
    first_num = float(input("What's the first number?: "))
    second_num = float(input("What's the second number?: "))
    for symbols in operations:
        print(symbols)
    operation = input("Pick and operation: ")

    calculation_function = operations[operation]
    solution = calculation_function(first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {solution}")

    while con:
        if input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start over: ").lower() == "n":
            calculator()

        first_num = solution
        for symbols in operations:
            print(symbols)
        operation = input("Pick and operation: ")
        third_num = float(input("What is the new second number: "))
        calculation_function = operations[operation]
        solution = calculation_function(first_num, third_num)
        print(f"{first_num} {operation} {third_num} = {solution}")


calculator()
