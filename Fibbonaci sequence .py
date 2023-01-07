d = int(input("Enter the amount of numbers: "))
m = 0
n = 1
new = [0, 1]
for x in range(d-2):
    fib = new[m] + new[n]
    new.append(fib)
    m += 1
    n += 1
for x in new:
    print(x)
