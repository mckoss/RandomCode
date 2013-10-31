from math import sqrt

def factors(x):
    fin = []
    for i in range(2, int(sqrt(x) + 1)):
        if (x % i == 0):
            fin.append(i)
            fin.append(x / i)
    return sorted(fin)


def primes(x):
    fin = []
    facts = factors(x)
    for i in range(len(facts)):
        if(len(factors(facts[i])) == 0):
            fin.append(facts[i])
    return fin


print primes(600851475143)
