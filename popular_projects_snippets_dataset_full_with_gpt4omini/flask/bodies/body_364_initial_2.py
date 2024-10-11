from collections import UserDict # pragma: no cover

self = type('Mock', (UserDict,), {'accessed': False})() # pragma: no cover
key = 'sample_key' # pragma: no cover
default = 'default_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5353)
aux = super().setdefault(key, default)
_l_(5354)
exit(aux)
