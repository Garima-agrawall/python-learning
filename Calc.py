num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter Sign(+,-,*,/):")
if operator== "+":
    num=num1+num2
    print(f"{num1} + {num2} = {num}")
elif operator== "-":
    num=num1-num2
    print(f"{num1} - {num2} = {num}")
elif operator== "*":
    num=num1*num2
    print(f"{num1} * {num2} = {num}")
elif operator== "/":
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        num=num1/num2
        print(f"{num1} / {num2} = {num}")
else:
    print("Invalid")