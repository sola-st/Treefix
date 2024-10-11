import sys # pragma: no cover

class MockSuper:# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return 'mocked_value'# pragma: no cover
 # pragma: no cover
self = type('MockClass', (MockSuper,), {'accessed': False})() # pragma: no cover
key = 'test_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
