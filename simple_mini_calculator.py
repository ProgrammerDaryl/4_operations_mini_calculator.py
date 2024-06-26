#greet the user
#ask the user to input the first number
#ask the user to input the second number
#ask the user which operation to use
import pyfiglet
from colorama import Fore
from colorama import Back, Style
def mini_calculator():
    print("\n")
    greetings = pyfiglet.figlet_format("Hello User!", font = "slant")
    print(Fore.CYAN + greetings + Fore.RESET)

    #ask the user which operator
    operation = input("Please select an operator: +-*/  ")

    if operation == "+":
        try: 
            number_1 = float(input("Please enter your first number here: "))
            number_2 = float(input("Please enter your second number here: "))
        #tell the user he can't use a non-number
        except ValueError as error:
            print("Invalid input\n")
            print(error)
            print("Please try again\n")
            return
        finally:
            retain_message = "\nGood Luck! :)\n"
            print(retain_message)
    
        plus_operator = pyfiglet.figlet_format("\nAddition", font = "doom")
        print(Fore.YELLOW + plus_operator + Fore.RESET)
        sum = (f"Answer: {number_1 + number_2}")
        print(Fore.YELLOW + sum + Fore.RESET)
    
    elif operation == "-":
        try: 
            number_1 = float(input("Please enter your first number here: "))
            number_2 = float(input("Please enter your second number here: "))
        #tell the user he can't use a non-number
        except ValueError as error:
            print("Invalid input\n")
            print(error)
            print("Please try again\n")
            return
        finally:
            retain_message = "\nGood Luck! :)\n"
            print(retain_message)

        minus_operator = pyfiglet.figlet_format("\nSubtraction", font = "doom")
        print(Fore.RED + minus_operator + Fore.RESET)
        difference = (f"Answer: {number_1 - number_2}")
        print(Fore.RED + difference + Fore.RESET)
    
    elif operation == "*":
        try: 
            number_1 = float(input("Please enter your first number here: "))
            number_2 = float(input("Please enter your second number here: "))
        #tell the user he can't use a non-number
        except ValueError as error:
            print("Invalid input\n")
            print(error)
            print("Please try again\n")
            return
        finally:
            retain_message = "\nGood Luck! :)\n"
            print(retain_message)
        times_operator = pyfiglet.figlet_format("\nMultiplication", font = "doom")
        print(Fore.BLUE + times_operator + Fore.RESET)
        product = (f"Answer: {number_1 * number_2}")
        print(Fore.BLUE + product + Fore.RESET)

    elif operation == "/":
        try: 
            number_1 = float(input("Please enter your first number here: "))
            number_2 = float(input("Please enter your second number here: "))
        #tell the user he can't use a non-number
        except ValueError as error:
            print("Invalid input\n")
            print(error)
            print("Please try again\n")
            return
        #tell the user he can't divide a number by zero
        try:
            division_operator = pyfiglet.figlet_format("\nDivision", font = "doom")
            print(Fore.MAGENTA + division_operator + Fore.RESET)
            quotient = (f"Answer: {number_1 / number_2}")
            print(Fore.MAGENTA + quotient + Fore.RESET)
        except ZeroDivisionError as error:
            print("Equation's Invalid\n")
            print(error)
            print("\nPlease try again!")
            return
        finally:
            retain_message = "\nGood Luck! :)\n"
            print(retain_message)
            
    else:
        invalid_operator = "\nThe operator you entered is not valid!\n"
    
        print(Back.RED + invalid_operator + Back.RESET)
        return

proceed = True
while proceed:
    mini_calculator()
    while proceed:
        #ask the user if he/she wants to continue
        rerun = pyfiglet.figlet_format("\nDo you want to compute again y/n?:    ", font = "digital")
        styled_rerun = input(Fore.GREEN + rerun + Fore.RESET)
        if styled_rerun.lower() == "y":
            break
        elif styled_rerun.lower() == "n":
            proceed = False
            end_statement = pyfiglet.figlet_format("\nThank you for trusting me! :)", font = "slant")
            print(Fore.CYAN + end_statement + Fore.RESET)
        else:
            #remind the user that the inputted word is invalid
            invalid_statement = pyfiglet.figlet_format("The data you entered is invalid :(", font = "doom")
            print(Fore.LIGHTRED_EX + invalid_statement + Fore.RESET)
        continue
