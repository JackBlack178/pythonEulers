
from math import sqrt, ceil
def divisors(n):
    factors = 0
    for i in range(1, int(ceil(sqrt(n)))+1):
        if n % i == 0:
            factors +=2
        if i*i==n:
            factors -=1
    return factors

n = 1

number = startnumber = 1
for i in range(2,1000000):
    number += i
    if divisors(number) >= 500:
        print(number)
        break
