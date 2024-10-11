from collections import defaultdict # pragma: no cover

stuff = [type('MockObj', (object,), {'a': 1, 'b': 2, 'c_int': 5})(), type('MockObj', (object,), {'a': 1, 'b': 3, 'c_int': 10})()] # pragma: no cover
d = defaultdict(int) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5029934/defaultdict-of-defaultdict
from l3.Runtime import _l_
for x in stuff:
    _l_(1303)

    d[x.a][x.b] += x.c_int
    _l_(1302)

d = defaultdict(int)
_l_(1304)
for x in stuff:
    _l_(1306)

    d[x.a,x.b] += x.c_int
    _l_(1305)

