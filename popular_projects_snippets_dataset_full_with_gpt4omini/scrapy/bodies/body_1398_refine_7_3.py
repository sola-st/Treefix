import sys # pragma: no cover

self = type('Mock', (object,), {'__class__': type('MockClass', (object,), {})})() # pragma: no cover

import sys # pragma: no cover

class MockClass: pass # pragma: no cover
self = MockClass() # pragma: no cover
self.__class__ = type('MockClassWithInit', (MockClass,), {'__init__': lambda self: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/item.py
from l3.Runtime import _l_
aux = self.__class__(self)
_l_(5201)
exit(aux)
