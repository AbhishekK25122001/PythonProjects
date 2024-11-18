def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division by zero"
    return a/b
def calculator():
    print("Welcome to the calculator!")
    print("operations: +,-,*,/")

    while True:
        #input operations
        operation=input("Enter an operation (+ , - , * , / ) or 'q' to quit: ")
        if operation =='q':
            print("Good bye!")
            break

        if operation not in ['+','-','*','/']:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1=float(input("Enter 1st number: "))
            num2=float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid Input. Please Enter numbers only")
            continue

        #perform calculations
        if operation=='+':
            print("Result: ",add(num1,num2))
        elif operation=='-':
            print("Result: ",subtract(num1,num2))
        elif operation=='*':
            print("Result: ",multiply(num1,num2))
        elif operation=='/':
            print("Result: ",divide(num1,num2))

#Run the calculator
calculator()