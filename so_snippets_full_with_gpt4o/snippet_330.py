# Extracted from https://stackoverflow.com/questions/18946662/why-shouldnt-i-use-pypy-over-cpython-if-pypy-is-6-3-times-faster
C:\Users\User>python -m timeit -n10 -s"from sympy import isprime" "isprime(2**521-1);isprime(2**1279-1)"
10 loops, best of 3: 294 msec per loop

C:\Users\User>pypy -m timeit -n10 -s"from sympy import isprime" "isprime(2**521-1);isprime(2**1279-1)"
10 loops, best of 3: 1.33 sec per loop

from sympy import sieve
primes = list(sieve.primerange(1, 10**6))

