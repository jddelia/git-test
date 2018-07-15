#Project Euler problem 2

a = 1
b = 2
sum = 0

while sum < 4000000:
    if b % 2 == 0:
        sum += b
    if a % 2 == 0:
        sum += a
    a += b
    b += a
    print(a, b)

print()
print(sum)
