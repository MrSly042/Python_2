# cant handle numbers and punctuation
want = True
while want == True:
    new = []
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    li = str(alphabets)
    alpha = li.swapcase()
    user = input("Insert Input: ")
    j = 0
    non = []
    leng = len(user)
    while j < leng:
        if user[j] == " ":
            non.append(j)
        j += 1
    i = -1
    for var in user:
        if var == " ":
            continue
        if var.isupper() == True:
            pos = alpha.index(var)
            ind_rep = -(pos + 1)
            repl = alpha[ind_rep]
            new.append(repl)
            continue
        pos = alphabets.index(var)
        ind_rep = -(pos + 1)
        replace_with = alphabets[ind_rep]
        new.append(replace_with)
    if " " in user:
        for var in non:
            new.insert(var, " ")
    decode = "".join(new)
    print("Your message is:", decode)
    choice = ["Yes", "yes", "YES", "Y", "y", "affirmative", "Affirmative"]
    choice_2 = ["No", "NO", "no", "n", "N", "Negative", "negative"]
    users_option = input("Would you like to use the program again?: ")
    if users_option in choice:
        want = True
    elif users_option in choice_2:
        want = False
    elif users_option not in choice or choice_2:
        ite = 0
        while ite == 0:
            print("Sorry I don't recognize your option. Try again")
            users_option = input("Would you like to use the program again?: ")
            if users_option in choice or users_option in choice_2:
                ite += 1
        if users_option in choice: want = True
        else: want = False
print("Thank you for using my program !!!!")