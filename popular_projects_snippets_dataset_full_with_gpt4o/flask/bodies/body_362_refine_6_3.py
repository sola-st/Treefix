import sys # pragma: no cover

self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
key = 'example_key' # pragma: no cover

import sys # pragma: no cover

class SuperClass:# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return 'mocked_result'# pragma: no cover
# pragma: no cover
class Mock(SuperClass):# pragma: no cover
    accessed = False # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
