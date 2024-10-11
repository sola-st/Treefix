import dict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.some_attribute = 'example_value' # pragma: no cover
self.some_method = lambda: 'example_method_result' # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__dict__ = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
