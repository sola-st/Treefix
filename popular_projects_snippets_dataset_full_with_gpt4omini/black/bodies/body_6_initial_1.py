from typing import Any # pragma: no cover

self = type('Mock', (object,), {'__post_init__': lambda self: None})() # pragma: no cover
mode = 'default' # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
Line = type('Line', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
self.mode = mode
_l_(7929)
self.features = features
_l_(7930)
self.current_line: Line
_l_(7931)
self.__post_init__()
_l_(7932)
