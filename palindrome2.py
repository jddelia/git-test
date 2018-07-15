#Largest palindrome of two 3 digit numbers.

def palindrome(a, b):
    x = 999
    n = 100
    y = 100
    z = 999
    while a > (b - 1):
        mult = a * b
        multstring = str(mult)
        if multstring[:] == multstring[::-1]:
            print(mult)
        x -= 1
        while b < (a + 1):
            mult2 = b * a
            mult2string = str(mult2)
            if mult2string[:] == mult2string[::-1]:
                print(mult2)
            b += 1
            if b == a:
                b = 9

palindrome(1000, 99)
