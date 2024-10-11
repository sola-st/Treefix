# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
from l3.Runtime import _l_
try:
    import sys
    _l_(2457)

except ImportError:
    pass
sys.setrecursionlimit(1500)
_l_(2458)

