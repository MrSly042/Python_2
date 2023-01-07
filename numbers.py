a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")
numbers = [a, b, c]
iter = 0
other = iter + 1
while iter < 2:
    if numbers[iter] > numbers[other]:
        biggest = numbers[iter]
    else: biggest = numbers[other] 
    iter +=1
    other +=1

print("THE BIGGEST NUMBER IS " + str(biggest))