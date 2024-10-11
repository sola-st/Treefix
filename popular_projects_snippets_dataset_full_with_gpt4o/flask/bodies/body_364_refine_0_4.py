self = type('Mock', (object,), {'accessed': True})() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_default' # pragma: no cover

class BaseDict(dict): # pragma: no cover
    def setdefault(self, key, default=None): # pragma: no cover
        return super().setdefault(key, default) # pragma: no cover
 # pragma: no cover
self = type('Mock', (BaseDict,), {'accessed': True})() # pragma: no cover
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
