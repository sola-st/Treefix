import types # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover

import sys # pragma: no cover

class MockClass: pass # pragma: no cover
self = MockClass() # pragma: no cover
self.__class__ = MockClass # pragma: no cover
self.__class__.__init__ = lambda self: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/item.py
from l3.Runtime import _l_
aux = self.__class__(self)
_l_(5201)
exit(aux)
