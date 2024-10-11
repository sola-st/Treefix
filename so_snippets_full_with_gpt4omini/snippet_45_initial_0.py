def my_crappy_range(n): return (i for i in range(n)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3
from l3.Runtime import _l_
a = range(5)
_l_(1389)
print(list(a))
_l_(1390)
[0, 1, 2, 3, 4]
_l_(1391)
print(list(a))
_l_(1392)
[0, 1, 2, 3, 4]
_l_(1393)

b = my_crappy_range(5)
_l_(1394)
print(list(b))
_l_(1395)
[0, 1, 2, 3, 4]
_l_(1396)
print(list(b))
_l_(1397)
[]
_l_(1398)
try:
    import collections.abc
    _l_(1400)

except ImportError:
    pass
isinstance(a, collections.abc.Sequence)
_l_(1401)
True
_l_(1402)

a[3]         # indexable
_l_(1403)         # indexable
3
_l_(1404)
len(a)       # sized
_l_(1405)       # sized
5
_l_(1406)
3 in a       # membership
_l_(1407)       # membership
True
_l_(1408)
reversed(a)  # reversible
_l_(1409)  # reversible
a.index(3)   # implements 'index'
_l_(1410)   # implements 'index'
3
_l_(1411)
a.count(3)   # implements 'count'
_l_(1412)   # implements 'count'
1
_l_(1413)

