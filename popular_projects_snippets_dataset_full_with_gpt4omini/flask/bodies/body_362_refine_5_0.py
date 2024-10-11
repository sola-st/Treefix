from collections import UserDict # pragma: no cover

class Mock(UserDict): # pragma: no cover
    def __getitem__(self, key): return 'value' # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.accessed = False # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return 'value' # pragma: no cover
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
