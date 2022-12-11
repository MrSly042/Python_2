#Caps and small letters seen as different
user = list(input("Enter the string: "))
for var in user:
    a = user.count(var)
    if a > 1:
        print("Deja Vu")
        break
if a== 1:
    print("Unique")