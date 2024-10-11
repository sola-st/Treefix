# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
from l3.Runtime import _l_
num_list[-9:]
_l_(13030)

sequence[start:stop:step]
_l_(13031)

list_copy = sequence[:]
_l_(13032)

del my_list[:]
_l_(13033)

last_nine_slice = slice(-9, None)
_l_(13034)

list(range(100))[last_nine_slice]
_l_(13035)
[91, 92, 93, 94, 95, 96, 97, 98, 99]
_l_(13036)
try:
    from itertools import islice
    _l_(13038)

except ImportError:
    pass
islice(reversed(range(100)), 0, 9)
_l_(13039)

list(islice(reversed(range(100)), 0, 9))
_l_(13040)
[99, 98, 97, 96, 95, 94, 93, 92, 91]
_l_(13041)

