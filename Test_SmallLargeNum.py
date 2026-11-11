i=1
while i<=5:
    num=int(input("Enter a number:"))
    if i==1:
        large=num
        small=num
    else:
        if num>large:
            large=num
        if num<small:
            small=num
    i+=1
print(large)
print(small)