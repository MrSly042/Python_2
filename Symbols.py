#Adjust to include caps
i = 0
new = []
liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
lis = str(liste)
liste_1 = lis.swapcase()
user = list(input("Enter the text: "))
a = len(user)
#print(a)
while i < a:
    word = user[i]
    if word in liste or word in liste_1:
        new.append(word)
    i += 1
#print(new)
ano = "".join(new)
print(ano)