

username=input("Enter Username:")
password=input("Enter your password:")
if username=="admin":
    if password=="11111":
        print("login sucessfuly")
    else:
        print("wrong password!")
else:
    print("User not found")