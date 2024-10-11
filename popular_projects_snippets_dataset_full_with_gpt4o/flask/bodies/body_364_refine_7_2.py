self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
key = 'some_key' # pragma: no cover
default = 'some_default_value' # pragma: no cover

from collections import defaultdict # pragma: no cover

class Base: # pragma: no cover
    def setdefault(self, key, default): # pragma: no cover
        return defaultdict(lambda: default).setdefault(key) # pragma: no cover
self = type('Mock', (Base,), {'accessed': True})() # pragma: no cover
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
