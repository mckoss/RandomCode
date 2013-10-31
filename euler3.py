from math import sqrt

def factors(x):
    fin = []
    i = 2
    while i <= sqrt(x):
        if (x % i == 0):
            fin.append(i)
            while (x % i == 0):
                x = x / i
        i += 1
    if x != 1:
        fin.append(x)
    return fin


def primes(x):
    return factors(x)[-1]


print factors(600851475143)
print primes(600851475143)
