_context = None # pragma: no cover
def _create_context():# pragma: no cover
    global _context# pragma: no cover
    _context = 'some_context_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
from l3.Runtime import _l_
"""Returns a singleton context object."""
if _context is None:
    _l_(21363)

    _create_context()
    _l_(21362)
aux = _context
_l_(21364)
exit(aux)
