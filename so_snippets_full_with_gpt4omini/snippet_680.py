# Extracted from https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
x = [ [ 'a', 'b'], ['c'] ]
for el in reduce(lambda a,b: a+b, x, []):
__main__:1: DeprecationWarning: reduce() not supported in 3.x; use functools.reduce()
a
b
c
import functools
for el in functools.reduce(lambda a,b: a+b, x, []):
a
b
c


