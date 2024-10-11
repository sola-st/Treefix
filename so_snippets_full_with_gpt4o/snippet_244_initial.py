# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
from l3.Runtime import _l_
try:
    import sys
    _l_(13603)

except ImportError:
    pass
x = 2
_l_(13604)
sys.getsizeof(x)
_l_(13605)
24
_l_(13606)
sys.getsizeof(sys.getsizeof)
_l_(13607)
32
_l_(13608)
sys.getsizeof('this')
_l_(13609)
38
_l_(13610)
sys.getsizeof('this also')
_l_(13611)
48
_l_(13612)

