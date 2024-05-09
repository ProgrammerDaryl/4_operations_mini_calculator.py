#greet the user
#ask the user to input the first number
#ask the user to input the second number
#ask the user which operation to use
def mini_calculator():
    print("Hello User!")
    number_1 = float(input("Please enter your first number here: "))
    number_2 = float(input("Please enter your second number here: "))
    operation = input("Please select an operator: +-*/  ")

    if operation == "+":
        answer = number_1 + number_2
    
    elif operation == "-":
        answer = number_1 - number_2
        



