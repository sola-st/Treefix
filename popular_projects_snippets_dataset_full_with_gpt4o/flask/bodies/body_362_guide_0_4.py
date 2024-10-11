import sys # pragma: no cover

class MockSuper:# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return f"Value for {key}" # pragma: no cover
type('MockSelf', (object,), {'accessed': False, '__class__.super': MockSuper}) # pragma: no cover
key = 'example_key' # pragma: no cover
aux = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
