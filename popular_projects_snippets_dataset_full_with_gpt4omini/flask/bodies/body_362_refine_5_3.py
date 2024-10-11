from collections import UserDict # pragma: no cover

class Mock(UserDict): # pragma: no cover
    def __getitem__(self, key): return 'value' # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover

class Mock: pass # pragma: no cover

self = type('MockWithGetItem', (object,), {'accessed': False, '__getitem__': lambda self, key: 'value'})() # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
