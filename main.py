#Simple python script to perform simple calculations
# Created by Jasmine


#Function to ask if the user wants to calculate
def ask_calculate(prompt):
    while True:
        try: 
            x = input(f"Would you like to calculate {prompt} (Y/N) -> ").strip().upper() # strip before making it upper
        except KeyboardInterrupt: #just quit if someone wants to ctrl c 
            exit()
        if x in ["N", "NO"]: #maybe try to make things lower, that's conventional
            print("＊*•̩̩͙✩•̩̩͙*˚　Bye Bye　˚*•̩̩͙✩•̩̩͙*˚＊")
            exit()
        elif x in ["Y", "YES"]:
            break
        else:
            print("Input Error: not y or n")

#Function to get a number from the user
def get_number(order):
    while True:
        try:
            return float(input(f"Enter {order} number -> "))
        except ValueError:
            print("Input Error: not a number.\n")

#Function to get a number from the user
def get_operator():
    operator = ("+", "-", "*", "/") #define a tuple of all operators
    while True:
        x = input("Enter operator (+, -, *. /) -> ").strip() #always strip 
        if x not in operator:
            print("Operator invalid.\n")
            continue
        else:
            return x #just return the operator 

def result(x, y, operator):
    return eval(f"{x} {operator} {y}") #no need to use if else or function , eval is easier

#Function to calculate, check for division by 0, and print result
def calculate(x, y, operator):
    if (operator == "/" and y == 0):
        print("Input Error: Division by zero")
        return
    print(f"\n{x} {operator} {y} = {result(x, y, operator)}\n\n") #call result


#Introducing program and asking if they want to calculate
print("\n\nThis program performs addition, subtraction, multiplication, and division.\n\n")
ask_calculate("?")

#Performing calculation
while True:
    try:
        x = get_number("first")          
        operator = get_operator()
        y = get_number("second")
        calculate(x, y, operator)
        ask_calculate("again?")
    except KeyboardInterrupt: # ctrl c just exits the program
        exit()
# added some new lines to make things a bit cleaner, made it little easier, cleaning all the complex things
# Thanks, have a nice day.

