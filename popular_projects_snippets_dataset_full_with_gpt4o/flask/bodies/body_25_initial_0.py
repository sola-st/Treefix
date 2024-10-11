exc_value = 'example_value' # pragma: no cover
self = type('Mock', (object,), {'pop': lambda self, x: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.pop(exc_value)
_l_(19392)
