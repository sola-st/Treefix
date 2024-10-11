from typing import Dict, Any # pragma: no cover

self = type('Mock', (object,), {'__repr__': lambda s: 'mock_repr', '__dict__': {'key': 'value'}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
