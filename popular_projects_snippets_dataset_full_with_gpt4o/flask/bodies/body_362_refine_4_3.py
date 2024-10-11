self = type('Mock', (object,), {'__getitem__': lambda self, key: 'mocked_result', 'accessed': True})() # pragma: no cover
key = 'test_key' # pragma: no cover

class BaseClass:# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return 'mocked_result'# pragma: no cover
 # pragma: no cover
class MockClass(BaseClass):# pragma: no cover
    accessed = True# pragma: no cover
 # pragma: no cover
self = MockClass() # pragma: no cover
key = 'test_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
