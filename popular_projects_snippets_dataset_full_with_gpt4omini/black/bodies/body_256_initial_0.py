from typing import Callable, Any # pragma: no cover

_out = lambda message, nl=True, **styles: print(message, end='\n' if nl else '', **styles) # pragma: no cover
message = 'Hello, World!' # pragma: no cover
nl = True # pragma: no cover
styles = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
_out(message, nl=nl, **styles)
_l_(5809)
