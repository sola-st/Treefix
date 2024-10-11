from typing import Dict # pragma: no cover

self = type('Mock', (object,), {'__repr__': lambda s: 'Mock instance', '__class__': type('MockClass', (object,), {}), '__dict__': {}})() # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__dict__ = {} # pragma: no cover
self.__repr__ = lambda: 'Mock representation' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
