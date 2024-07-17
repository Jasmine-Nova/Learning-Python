# Arithmetic calculator in Python
# Created by Jasmine


#Function to ask if the user wants to calculate
def ask_calculate(prompt):
    while True:
        try: 
            x = input(f"\nWould you like to calculate{prompt} (Y/N) -> ").strip().upper() # strip before making it upper
        except KeyboardInterrupt: #quit if someone wants to ctrl c 
            exit()
        if x in ["N", "NO"]: #maybe try to make things lower, that's conventional
            print("＊*•̩̩͙✩•̩̩͙*˚　Bye Bye　˚*•̩̩͙✩•̩̩͙*˚＊\n")
            exit()
        elif x in ["Y", "YES"]:
            break
        else:
            print("Input Error: Please enter 'Y' or 'N'.")

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
        if x in operator:
            return x #just return the operator
        else:
            print("Input Error: Please enter '+', '-', '*', or '/'.")

#Function to calculate, check for division by 0, and print result
def calculate(x, y, operator):
    if not (operator == "/" and y == 0):
        print(f"\n{x} {operator} {y} = {eval(f"{x} {operator} {y}")}") #call result
    else:   
        print("Input Error: Division by zero")



#Introducing program and asking if they want to calculate
print("\n\nThis program performs addition, subtraction, multiplication, and division.\n")
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
