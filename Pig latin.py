#pig latin
import re
user = input("Enter human language: ")
reg = re.split("\s", user)
output_1 = []
output_2 = []
for var in reg:
    lis = list(var)
    a = lis[0]
    b = lis.index(a)
    lis.pop(b)
    lis.append(a)
    lis.append("ay")
    output_1.append(lis)
    q = "".join(lis)
    output_2.append(q)
final = " ".join(output_2)
print(final)