import dict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__class__.__name__ = 'MockClass' # pragma: no cover
self.__dict__ = {} # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.attr = 'value' # pragma: no cover
dict_repr = builtins.dict(self.__dict__).__repr__() # pragma: no cover
exit_message = f'<{type(self).__name__} {dict_repr}>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
