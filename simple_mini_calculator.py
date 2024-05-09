#greet the user
#ask the user to input the first number
#ask the user to input the second number
#ask the user which operation to use
import pyfiglet
from colorama import Fore
def mini_calculator():
    print("\n")
    greetings = pyfiglet.figlet_format("Hello User!", font = "slant")
    print(Fore.CYAN + greetings + Fore.RESET)

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
        plus_operator = pyfiglet.figlet_format("\nADDITION", font = "doom")
        print(Fore.LIGHTYELLOW_EX + plus_operator + Fore.BLACK)
        sum = (f"Answer: {number_1 + number_2}")
        print(sum)
    
    elif operation == "-":
        minus_operator = pyfiglet.figlet_format("\nSUBTRACTION", font = "doom")
        print(Fore.RED + minus_operator + Fore.BLACK)
        difference = (f"Answer: {number_1 - number_2}")
        print(difference)
    
    elif operation == "*":
        times_operator = pyfiglet.figlet_format("\nMULTIPLICATION", font = "doom")
        print(Fore.BLUE + times_operator + Fore.BLACK)
        product = (f"Answer: {number_1 * number_2}")
        print(product)

    elif operation == "/":
        #tell the user he can't divide a number by zero
        try:
            division_operator = pyfiglet.figlet_format("\nDIVISION", font = "doom")
            print(Fore.MAGENTA + division_operator + Fore.BLACK)
            quotient = (f"Answer: {number_1 / number_2}")
            print(quotient)
        except ZeroDivisionError as error:
            print("Equation's Invalid\n")
            print(error)
            print("\nPlease try again!")
            return
            
    
    else:
        invalid_operator = "The operator you entered is not valid!"
    
        print(invalid_operator)
proceed = True
while proceed:
    mini_calculator()
    while proceed:
        rerun = pyfiglet.figlet_format("\nDo you want to compute again y/n?:    ", font = "bubble")
        styled_rerun = input(Fore.GREEN + rerun + Fore.BLACK)
        if rerun.lower() == "y":
            break
        elif rerun.lower() == "n":
            proceed = False
            end_statement = pyfiglet.figlet_format("\nThank you for trusting me! :)", font = "slant")
            print(Fore.CYAN + end_statement + Fore.BLACK)
        else:
            invalid_statement = pyfiglet.figlet_format("The data you entered is invalid :(", font = "doom")
            print(Fore.LIGHTRED_EX + invalid_statement + Fore.BLACK)
        continue

