key = 'example_key' # pragma: no cover
self = type('Mock', (object,), {'accessed': False, '__getitem__': lambda self, k: 'example_value'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
