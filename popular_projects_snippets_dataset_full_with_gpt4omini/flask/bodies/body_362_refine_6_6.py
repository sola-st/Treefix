import collections # pragma: no cover

self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
key = 'example_key' # pragma: no cover

from collections.abc import MutableMapping # pragma: no cover

class Mock(MutableMapping): # pragma: no cover
    def __init__(self): # pragma: no cover
        self._data = {'example_key': 'value'} # pragma: no cover
        self.accessed = False # pragma: no cover
    def __getitem__(self, key): return self._data[key] # pragma: no cover
    def __setitem__(self, key, value): self._data[key] = value # pragma: no cover
    def __delitem__(self, key): del self._data[key] # pragma: no cover
    def __iter__(self): return iter(self._data) # pragma: no cover
    def __len__(self): return len(self._data) # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
