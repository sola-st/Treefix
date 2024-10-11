self = type('Mock', (object,), {'__class__': None})() # pragma: no cover
self.__class__ = type('MockClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/item.py
from l3.Runtime import _l_
aux = self.__class__(self)
_l_(16363)
exit(aux)
