# Extracted from https://stackoverflow.com/questions/8537916/how-do-i-prepend-to-a-short-python-list
Python 2.7.8

In [1]: %timeit ([1]*1000000).insert(0, 0)
100 loops, best of 3: 4.62 ms per loop

In [2]: %timeit ([1]*1000000)[0:0] = [0]
100 loops, best of 3: 4.55 ms per loop

In [3]: %timeit [0] + [1]*1000000
100 loops, best of 3: 8.04 ms per loop

