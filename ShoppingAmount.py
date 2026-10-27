amount=int(input("Enter Your Amount:"))
if amount >=5000:
    print("Discount 20%")
    pay=amount*20/100
    print("Total Amount:",amount)
    print("After Discount:",pay)
    print("Final Amount:",amount-pay)
elif amount < 5000 and amount>=2000:
    print("Discount 10%")
    pay=amount*10/100
    print("Total Amount:",amount)
    print("After Discount:",pay)
    print("Final Amount:",amount-pay)
elif amount <2000 and amount>0:
    print("No Discount")
    print("Final Amount:",amount)
else:
    print("Invalid")