from typing import Any # pragma: no cover

class MockBase: # pragma: no cover
    def __getitem__(self, key: Any) -> Any: # pragma: no cover
        return {'mock_key': 'mock_value'}.get(key, None) # pragma: no cover
 # pragma: no cover
class Mock(MockBase): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.accessed = False # pragma: no cover
 # pragma: no cover
mock_instance = Mock() # pragma: no cover
self = mock_instance # pragma: no cover
key = 'mock_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
