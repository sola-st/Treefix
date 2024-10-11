import sys # pragma: no cover

class MockSuperClass:# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return 'mocked_value'# pragma: no cover
 # pragma: no cover
MockSelf = type('MockSelf', (MockSuperClass,), {'accessed': False}) # pragma: no cover
self = MockSelf() # pragma: no cover
key = 'mock_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
