from itertools import islice # pragma: no cover

num_list = list(range(100)) # pragma: no cover
sequence = list(range(100)) # pragma: no cover
start = 0 # pragma: no cover
stop = 9 # pragma: no cover
step = 1 # pragma: no cover
my_list = list(range(10)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
from l3.Runtime import _l_
num_list[-9:]
_l_(1440)

sequence[start:stop:step]
_l_(1441)

list_copy = sequence[:]
_l_(1442)

del my_list[:]
_l_(1443)

last_nine_slice = slice(-9, None)
_l_(1444)

list(range(100))[last_nine_slice]
_l_(1445)
[91, 92, 93, 94, 95, 96, 97, 98, 99]
_l_(1446)
try:
    from itertools import islice
    _l_(1448)

except ImportError:
    pass
islice(reversed(range(100)), 0, 9)
_l_(1449)

list(islice(reversed(range(100)), 0, 9))
_l_(1450)
[99, 98, 97, 96, 95, 94, 93, 92, 91]
_l_(1451)

