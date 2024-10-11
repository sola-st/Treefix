import sys # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__class__ = Mock # pragma: no cover

import sys # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): pass # pragma: no cover
self = Mock() # pragma: no cover
self.__class__ = type('MockClass', (Mock,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/item.py
from l3.Runtime import _l_
aux = self.__class__(self)
_l_(5201)
exit(aux)
