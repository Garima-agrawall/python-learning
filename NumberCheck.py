num=int(input("Enter a number:"))
if num%2==0 and num >0:
    print("Positive Even")
elif num%2!=0 and num >0:
    print("Positive Odd")
elif num==0 :
    print("Zero")
else:
    print("Negative Number")