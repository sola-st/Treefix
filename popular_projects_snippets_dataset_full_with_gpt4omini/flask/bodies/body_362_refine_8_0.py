from collections.abc import MutableMapping # pragma: no cover

class Mock(MutableMapping): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.accessed = False # pragma: no cover
        self.data = {} # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return self.data.get(key, None) # pragma: no cover
    def __setitem__(self, key, value): # pragma: no cover
        self.data[key] = value # pragma: no cover
    def __delitem__(self, key): # pragma: no cover
        del self.data[key] # pragma: no cover
    def __iter__(self): # pragma: no cover
        return iter(self.data) # pragma: no cover
    def __len__(self): # pragma: no cover
        return len(self.data) # pragma: no cover
self = Mock() # pragma: no cover
key = 'test_key' # pragma: no cover

from collections import UserDict # pragma: no cover

class Mock(UserDict): # pragma: no cover
    def __init__(self): # pragma: no cover
        super().__init__() # pragma: no cover
        self.accessed = False # pragma: no cover
self = Mock() # pragma: no cover
self['example_key'] = 'example_value' # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
