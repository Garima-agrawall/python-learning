num = int(input("Enter Your Marks :"))
if num >90 and num <100:
    print("Grade A")
elif num >75 and num<89:
    print("Grade B")
elif num > 60 and num <74:
    print("Grade C")
elif num>40 and num<59:
    print("Grade D")
elif num>0 and num<40:
    print("Fail")
else:
    print("Invalid Marks")  