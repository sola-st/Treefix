from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'accessed': True, 'setdefault': defaultdict(lambda: 'default').setdefault})() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_default' # pragma: no cover

from collections import defaultdict # pragma: no cover

class BaseClass:# pragma: no cover
    def setdefault(self, key, default):# pragma: no cover
        return 'mock_value' # pragma: no cover
class DerivedClass(BaseClass):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.accessed = False # pragma: no cover
self = DerivedClass() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_default' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22601)
aux = super().setdefault(key, default)
_l_(22602)
exit(aux)
