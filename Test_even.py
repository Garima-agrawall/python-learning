num = int(input("Enter a number:"))
count=0
i=1
while i<=num:
    if i%2==0:
        count=count+1
    i=i+1
print(count)