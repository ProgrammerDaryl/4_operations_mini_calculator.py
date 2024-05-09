#greet the user
#ask the user to input the first number
#ask the user to input the second number
#ask the user which operation to use
def mini_calculator():
    print("\n")
    print("Hello User!")
    number_1 = float(input("Please enter your first number here: "))
    number_2 = float(input("Please enter your second number here: "))
    operation = input("Please select an operator: +-*/  ")

    if operation == "+":
        answer = number_1 + number_2
        print(answer)
    
    elif operation == "-":
        answer = number_1 - number_2
        print(answer)
    
    elif operation == "*":
        answer = number_1 * number_2
        print(answer)

    elif operation == "/":
        answer = (number_1 / number_2)
        print(answer)
    
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
        else:
            print("The data you entered is invalid:(")
        continue

