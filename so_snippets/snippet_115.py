# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/44834/what-does-all-mean-in-python
from l3.Runtime import _l_
try:
    from foo import *
    _l_(1371)

except ImportError:
    pass

__all__ = ('some_name',)
_l_(1372)

