class my_crappy_range: # pragma: no cover
    def __init__(self, n): # pragma: no cover
        self.n = n # pragma: no cover
        self.iterated = False # pragma: no cover
    def __iter__(self): # pragma: no cover
        if self.iterated: # pragma: no cover
            return iter([]) # pragma: no cover
        else: # pragma: no cover
            self.iterated = True # pragma: no cover
            return iter(range(self.n)) # pragma: no cover
    def __len__(self): # pragma: no cover
        return self.n # pragma: no cover
    def __getitem__(self, idx): # pragma: no cover
        return list(range(self.n))[idx] # pragma: no cover
    def index(self, value): # pragma: no cover
        return list(range(self.n)).index(value) # pragma: no cover
    def count(self, value): # pragma: no cover
        return list(range(self.n)).count(value) # pragma: no cover

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

