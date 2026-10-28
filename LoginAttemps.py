password="python123"

attemp=0
while attemp<3:
    password=input("Enter password:")
    if password=="python123":
        print("Login Successful")
        break
    else:
        print("Wrong Password")
        print("Try Again")
        attemp=attemp+1
if attemp==3:
    print("Account Locked")