from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover

 # pragma: no cover

class MockClass: pass # pragma: no cover
self = MockClass() # pragma: no cover
self.__dict__ = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
