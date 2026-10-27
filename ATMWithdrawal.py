account_balance=int(input("Enter your account balance:"))
withdrawal_amount=int(input("Enter withdrawal amount:"))
if withdrawal_amount <=0:
    print("Invalid Amount")
elif account_balance <=0:
    print("Insufficient Balance")
elif withdrawal_amount >account_balance:
    print("Insufficient Balance")
else:
    remaining_amount=account_balance-withdrawal_amount
    print("remaining balance",remaining_amount)