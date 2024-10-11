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

