# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
from l3.Runtime import _l_
try:
    import sys
    _l_(2203)

except ImportError:
    pass
x = 2
_l_(2204)
sys.getsizeof(x)
_l_(2205)
24
_l_(2206)
sys.getsizeof(sys.getsizeof)
_l_(2207)
32
_l_(2208)
sys.getsizeof('this')
_l_(2209)
38
_l_(2210)
sys.getsizeof('this also')
_l_(2211)
48
_l_(2212)

