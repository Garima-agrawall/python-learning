i=1
while i<=5:
    
    num=int(input("Enter number:"))
    if i==1:
        largest=num
        smallest=num
    else:
        if num >largest:
            largest=num
            
    
        if num<smallest:
            smallest=num
            
    i=i+1

print("Smallest:",smallest) 
print("Largest:",largest)
