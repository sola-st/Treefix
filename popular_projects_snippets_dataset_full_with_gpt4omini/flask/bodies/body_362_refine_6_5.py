import collections # pragma: no cover

self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
key = 'example_key' # pragma: no cover

from collections import UserDict # pragma: no cover

class Mock(UserDict): # pragma: no cover
    def __init__(self): # pragma: no cover
        super().__init__() # pragma: no cover
        self.accessed = False # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover
self[key] = 'example_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
