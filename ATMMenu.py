balance=5000
while True:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Exit")

    choice=int(input("Enter you choice:"))
    if choice==1:
        print(f"The balance in your account is {balance}")
    elif choice==2:
        deposit_amount=int(input("Enter amount you deposit:"))
        balance=deposit_amount+balance
        print(f"Now your balance is {balance}")
    elif choice==3:
        withdraw_amount=int(input("Enter amount you want to withdraw:"))
        if balance<withdraw_amount:
            print("Insufficient Amount")
        elif withdraw_amount<=balance:
            balance=balance-withdraw_amount
            print(f"Now your balance is {balance}")
    elif choice==4:
        print("Thank you for using our ATM service")
        break
    else:
        print("Invalid choice")