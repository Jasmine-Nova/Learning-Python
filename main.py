# Arithmetic calculator in Python
# Created by Jasmine

#Function to ask if the user wants to calculate
def ask_calculate(prompt):
    while True:
        try: 
            x = input(f"Would you like to calculate{prompt} (Y/N) -> ").strip().upper() # strip before making it upper
        except KeyboardInterrupt: #quit if someone wants to ctrl c 
            exit()
        if x in ["N", "NO"]: #maybe try to make things lower, that's conventional
            print("＊*•̩̩͙✩•̩̩͙*˚　Bye  Bye　˚*•̩̩͙✩•̩̩͙*˚＊\n")
            exit()
        elif x in ["Y", "YES"]:
            break
        else:
            print("Input Error: Please enter 'Y' or 'N'.\n")

#Function to get a number from the user
def get_number(order):
    while True:
        try:
            return float(input(f"Enter {order} number -> "))
        except ValueError:
            print("Input Error: Please enter a number.")

#Function to get a number from the user
def get_operator():
    operator = ("+", "-", "*", "/") #define a tuple of all operators
    while True:
        x = input("Enter operator (+, -, *. /) -> ").strip() #always strip 
        if x not in operator:
            print("Input Error: Please enter '+', '-', '*', or '/'.")
            continue
        else:
            return x #just return the operator

#Function to calculate, check for division by 0, and print result
def calculate(x, y, operator):
    if (operator == "/" and y == 0):
        print("Input Error: Division by zero")
        return
    result = eval(f"{x} {operator} {y}")
    print(f"\n{x} {operator} {y} = {result}\n") #call result


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
        ask_calculate(" again?")
    except KeyboardInterrupt: # ctrl c exits the program
        exit()
