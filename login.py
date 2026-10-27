username=input("Enter Username:")
password=input("Enter Password:")
if username=="admin":
    if password=="1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User not found")