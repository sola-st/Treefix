from typing import Optional # pragma: no cover

_context: Optional[object] = None # pragma: no cover
_create_context = lambda: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
from l3.Runtime import _l_
"""Returns a singleton context object."""
if _context is None:
    _l_(8913)

    _create_context()
    _l_(8912)
aux = _context
_l_(8914)
exit(aux)
