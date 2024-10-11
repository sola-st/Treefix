import sys # pragma: no cover

self = type('Mock', (object,), {'accessed': True, '__getitem__': lambda self, key: 'mock_value'})() # pragma: no cover
key = 'mock_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
