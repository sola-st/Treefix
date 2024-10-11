import array # pragma: no cover

arr = array.array('i') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/518021/is-arr-len-the-preferred-way-to-get-the-length-of-an-array-in-python
from l3.Runtime import _l_
try:
    import array
    _l_(2279)

except ImportError:
    pass
arr = array.array('i')
_l_(2280)
arr.append('2')
_l_(2281)
arr.__len__()
_l_(2282)
1
_l_(2283)
len(arr)
_l_(2284)
1
_l_(2285)

