self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_value' # pragma: no cover

class SuperClass:# pragma: no cover
    def setdefault(self, key, default=None):# pragma: no cover
        return default # pragma: no cover
class Mock(SuperClass):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.accessed = True # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_default' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22601)
aux = super().setdefault(key, default)
_l_(22602)
exit(aux)
