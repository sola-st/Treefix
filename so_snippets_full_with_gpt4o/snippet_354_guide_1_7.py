import array # pragma: no cover

arr = array.array('i') # pragma: no cover
try:# pragma: no cover
    arr.append('2')# pragma: no cover
except TypeError:# pragma: no cover
    pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/518021/is-arr-len-the-preferred-way-to-get-the-length-of-an-array-in-python
from l3.Runtime import _l_
try:
    import array
    _l_(13712)

except ImportError:
    pass
arr = array.array('i')
_l_(13713)
arr.append('2')
_l_(13714)
arr.__len__()
_l_(13715)
1
_l_(13716)
len(arr)
_l_(13717)
1
_l_(13718)

