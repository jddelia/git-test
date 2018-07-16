''' This program calculates the largest prime of a
    specified number. '''

import math

''' This function finds primes up to specified number and
    places them in a list. '''

def primes(n):
    primes_lst = []
    check = 0
    for i in range(n, 2, -1):
        for n in range(2, i):
            if i % math.sqrt(n) == 0:
                check += 1
                break
        if check == 1:
            check = 0
            continue
        primes_lst.append(i)
    return primes_lst

prime_lst = primes(10000)   # Primes up to 10000

''' This function iterates through a reversed
    prime_lst, dividing input by each item in list.
    The first match is the largest prime. '''

def largest_prime(n):
    for i in sorted(prime_lst, reverse=True):
        if n % i == 0:
            return i

largest_prime(600851475143)
