self = type('Mock', (object,), {'accessed': True})() # pragma: no cover
key = 'sample_key' # pragma: no cover

class Mock(object): # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return 'mocked_result' # pragma: no cover
    accessed = True # pragma: no cover
class SubMock(Mock): # pragma: no cover
    def __init__(self): # pragma: no cover
        super(SubMock, self).__init__() # pragma: no cover
self = SubMock() # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
