from typing import Any # pragma: no cover
class CannotTransform: pass # pragma: no cover

CannotTransform = type('CannotTransform', (object,), {'__init__': lambda self, err_msg: None}) # pragma: no cover
err_msg = 'Transformation failed.' # pragma: no cover
Err = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""(T)ransform Err

    Convenience function used when working with the TResult type.
    """
cant_transform = CannotTransform(err_msg)
_l_(5682)
aux = Err(cant_transform)
_l_(5683)
exit(aux)
