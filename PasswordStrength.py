password=input("Enter Password:")
if len(password)>=8:
    print("Good length")
elif len(password)>=5:
    print("Medium length")
elif len(password)<5:
    print("Very short")