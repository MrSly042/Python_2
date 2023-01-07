user = input("Enter your name: ")
a = len(user)
if a < 4:
    raise Exception("Invalid Name")
else: print("Account Created")