Marks=int(input("Enter your mark:"))
if Marks>=90 and Marks<=100:
    print("Grade A")
elif Marks>=75 and Marks<=89:
    print("Grade B")
elif Marks>=60 and Marks<=74:
    print("Grade C")
elif Marks>=40 and Marks<=59:
    print("Grade D")
elif Marks<40 and Marks>=0:
    print("Fail")
else:
    print("Invalid Marks")