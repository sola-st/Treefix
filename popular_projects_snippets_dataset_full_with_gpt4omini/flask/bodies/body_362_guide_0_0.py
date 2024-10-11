from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.accessed = False # pragma: no cover
type('Base', (object,), {}) # pragma: no cover
super = lambda: SimpleNamespace(__getitem__=lambda key: 'value') # pragma: no cover
key = 'example' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
