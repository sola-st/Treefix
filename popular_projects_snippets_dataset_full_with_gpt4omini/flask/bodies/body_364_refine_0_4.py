from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'default_value' # pragma: no cover

from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'accessed': False})() # pragma: no cover
self.data = defaultdict(lambda: 'default_value') # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'default_value' # pragma: no cover
super = lambda: self.data # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5353)
aux = super().setdefault(key, default)
_l_(5354)
exit(aux)
