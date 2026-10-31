count_e=0
count_o=0
zero=0
i=0
while i <5:
    num=int(input("Enter a number:"))
    if num>0:
        count_e=count_e+1
     #   print("positive number:",count_e)
    elif num<0:
        count_o=count_o+1
       # print("negative number:",count_o)
    else:
        zero=zero+1
       # print("zero:",zero)
    i=i+1

print("positive number:",count_e)
print("negative number:",count_o)
print("zero:",zero)