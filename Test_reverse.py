num=int(input("Enter a number:"))
reverse=0
num1=num
while num>0:
    digit=num%10
    num=num//10
    reverse=reverse*10+digit
print(reverse)
if num1==reverse:
    print("The number is a palindrome")         
else:
    print("The number is not a palindrome") 
