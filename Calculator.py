#Calculator
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
cal=(input("Which Calculation you want to perform '+','-','*','/':"))
if cal =="+":
    print(num1+num2)
elif cal =="-":
    print(num1-num2)
elif cal =="*":
    print(num1*num2)
elif cal =="/":
    if num2==0:
        print("Division by zero is not allowed")
    else:
        print(num1/num2)
else:
    print("Invalid operation")
