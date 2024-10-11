self = type('Mock', (object,), {'_value': None})() # pragma: no cover
value = 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/rusty.py
from l3.Runtime import _l_
self._value = value
_l_(7928)
