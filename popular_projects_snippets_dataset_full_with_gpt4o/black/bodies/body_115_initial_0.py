value = 42 # pragma: no cover
self = type("Mock", (object,), {"_value": None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/rusty.py
from l3.Runtime import _l_
self._value = value
_l_(19711)
