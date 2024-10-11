# Extracted from https://stackoverflow.com/questions/4344017/how-can-i-get-the-concatenation-of-two-lists-in-python-without-modifying-either
import itertools
a = [1, 2, 3]
b = [4, 5, 6]
c = itertools.chain(a, b)

for i in c:
1
2
3
4
5
6

