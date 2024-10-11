# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3
from l3.Runtime import _l_
a = range(5)
_l_(13362)
print(list(a))
_l_(13363)
[0, 1, 2, 3, 4]
_l_(13364)
print(list(a))
_l_(13365)
[0, 1, 2, 3, 4]
_l_(13366)

b = my_crappy_range(5)
_l_(13367)
print(list(b))
_l_(13368)
[0, 1, 2, 3, 4]
_l_(13369)
print(list(b))
_l_(13370)
[]
_l_(13371)
try:
    import collections.abc
    _l_(13373)

except ImportError:
    pass
isinstance(a, collections.abc.Sequence)
_l_(13374)
True
_l_(13375)

a[3]         # indexable
_l_(13376)         # indexable
3
_l_(13377)
len(a)       # sized
_l_(13378)       # sized
5
_l_(13379)
3 in a       # membership
_l_(13380)       # membership
True
_l_(13381)
reversed(a)  # reversible
_l_(13382)  # reversible
a.index(3)   # implements 'index'
_l_(13383)   # implements 'index'
3
_l_(13384)
a.count(3)   # implements 'count'
_l_(13385)   # implements 'count'
1
_l_(13386)

