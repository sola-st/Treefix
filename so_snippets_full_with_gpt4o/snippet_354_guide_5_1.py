import array # pragma: no cover

class MockArray(array.array): # pragma: no cover
    def append(self, value): # pragma: no cover
        if not isinstance(value, int): # pragma: no cover
            raise TypeError('an integer is required (got type str)') # pragma: no cover
        super().append(value) # pragma: no cover
arr = MockArray('i') # pragma: no cover
try: arr.append('2') # pragma: no cover
except TypeError: pass # pragma: no cover

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

