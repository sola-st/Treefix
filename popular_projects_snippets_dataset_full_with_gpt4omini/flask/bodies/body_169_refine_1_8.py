import dict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__class__.__name__ = 'MockClass' # pragma: no cover
self.__dict__ = {} # pragma: no cover

class MockClass: pass # pragma: no cover
self = MockClass() # pragma: no cover
self.__dict__ = {} # pragma: no cover
def repr_func(self): return 'MockClass()' # pragma: no cover
self.__repr__ = repr_func.__get__(self) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
