import random # pragma: no cover

X = list(range(100)) # pragma: no cover
def prime(n):# pragma: no cover
    if n < 2:# pragma: no cover
        return False# pragma: no cover
    for i in range(2, int(n**0.5) + 1):# pragma: no cover
        if n % i == 0:# pragma: no cover
            return False# pragma: no cover
    return True # pragma: no cover
P = lambda x: x % 2 == 0 # pragma: no cover
f = lambda x: x**2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter
from l3.Runtime import _l_
[x for x in X if P(x)]
_l_(15068)

[f(x) for x in X if P(f(x))]
_l_(15069)

primes_cubed = [x*x*x for x in range(1000) if prime(x)]
_l_(15070)

prime_cubes = [x*x*x for x in range(1000) if prime(x*x*x)]
_l_(15071)

prime_cubes = filter(prime, [x*x*x for x in range(1000)])
_l_(15072)

