 # pragma: no cover
MockBase = type('MockBase', (object,), {'setdefault': lambda self, key, default: key + default})# pragma: no cover
 # pragma: no cover
self = type('Mock', (MockBase,), {'accessed': False})()# pragma: no cover
 # pragma: no cover
key = 'example_key'# pragma: no cover
 # pragma: no cover
default = '_default_value'# pragma: no cover
 # pragma: no cover
super = lambda: self# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22601)
aux = super().setdefault(key, default)
_l_(22602)
exit(aux)
