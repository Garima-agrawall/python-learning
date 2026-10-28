password=input("Enter your password:")
attemp=int(input("Enter the number of attempts:"))
if attemp>3:
    print("Account Locked")
elif password=="python":
    print("Login Successful")
else:
    print("Wrong Password")