num=int(input("Enter a number:"))
total=0
i=1
while i<=num:
    if i%2==0:
        total=total+i
        print(total)
    i=i+1
print(total)