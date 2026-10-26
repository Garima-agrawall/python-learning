num=int(input("Enter a year:"))
if num%4==0:
    if num%100==0:
        if num%400==0:
            print(num,"Leap Year")
        else:
            print(num,"Not Leap Year")
    else:
        print(num,"Not Leap Year")
else:
    print(num,"Leap Year")