from collections import defaultdict # pragma: no cover

stuff = [type('Mock', (object,), {'a': 'A', 'b': 1, 'c_int': 10})(), type('Mock', (object,), {'a': 'B', 'b': 2, 'c_int': 20})()] # pragma: no cover
d = defaultdict(lambda: defaultdict(int)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5029934/defaultdict-of-defaultdict
from l3.Runtime import _l_
for x in stuff:
    _l_(13337)

    d[x.a][x.b] += x.c_int
    _l_(13336)

d = defaultdict(int)
_l_(13338)
for x in stuff:
    _l_(13340)

    d[x.a,x.b] += x.c_int
    _l_(13339)

