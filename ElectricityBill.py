units=int(input("Enter your units:"))
if units<0:
    print("Invalid")
elif units>0 and units<=100:
    Bill=units*5
    print("Total Bill:",Bill)
elif units>100 and units<=200:
    Bill=units*7
    print("Total Bill:",Bill)
else:
    Bill=units*10
    print("Total Bill:",Bill)