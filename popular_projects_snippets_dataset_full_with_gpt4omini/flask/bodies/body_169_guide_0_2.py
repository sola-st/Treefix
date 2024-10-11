from typing import Any # pragma: no cover

self = type('Mock', (object,), {'__repr__': lambda self: 'MockRepresentation()'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
