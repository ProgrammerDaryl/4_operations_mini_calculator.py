#greet the user
#ask the user to input the first number
#ask the user to input the second number
#ask the user which operation to use
def mini_calculator():
    print("\n")
    print("Hello User!")

    #tell the user he can't use a non-number
    try: 
        number_1 = float(input("Please enter your first number here: "))
        number_2 = float(input("Please enter your second number here: "))
    except ValueError as error:
        print("Invalid input\n")
        print(error)
        print("Please try again\n")
        return

    operation = input("Please select an operator: +-*/  ")

    if operation == "+":
        print("\nADDITION")
        answer = number_1 + number_2
        print(answer)
    
    elif operation == "-":
        print("SUBTRACTION")
        answer = number_1 - number_2
        print(answer)
    
    elif operation == "*":
        print("MULTIPLICATION")
        answer = number_1 * number_2
        print(answer)

    elif operation == "/":
        #tell the user he can't divide a number by zero
        try:
            print("DIVISION")
            answer = (number_1 / number_2)
            print(answer)
        except ZeroDivisionError as error:
            print("You can't divide any number by zero(0)")
    
    else:
        answer = "The operator you entered is not valid!"
    
        print(f"Answer: {answer}\n")
proceed = True
while proceed:
    mini_calculator()
    while proceed:
        rerun = input("Do you want to compute again y/n?: ")
        if rerun.lower() == "y":
            break
        elif rerun.lower() == "n":
            proceed = False
            print("\nThank you for trusting me!")
        else:
            print("The data you entered is invalid:(")
        continue

