from dataclasses import dataclass # pragma: no cover
from typing import Any # pragma: no cover

@dataclass # pragma: no cover
class CannotTransform: # pragma: no cover
    err_msg: str = "Default error message" # pragma: no cover
 # pragma: no cover
err_msg = "An error occurred during transformation." # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, value: Any): # pragma: no cover
        self.value = value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""(T)ransform Err

    Convenience function used when working with the TResult type.
    """
cant_transform = CannotTransform(err_msg)
_l_(17095)
aux = Err(cant_transform)
_l_(17096)
exit(aux)
