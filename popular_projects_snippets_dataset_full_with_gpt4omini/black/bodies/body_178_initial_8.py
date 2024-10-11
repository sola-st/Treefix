from typing import Any # pragma: no cover

check = True # pragma: no cover
diff = False # pragma: no cover
color = False # pragma: no cover
cls = type('Mock', (object,), {'CHECK': 1, 'COLOR_DIFF': 2, 'DIFF': 3, 'YES': 4})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
if check and not diff:
    _l_(5011)

    aux = cls.CHECK
    _l_(5010)
    exit(aux)

if diff and color:
    _l_(5013)

    aux = cls.COLOR_DIFF
    _l_(5012)
    exit(aux)
aux = cls.DIFF if diff else cls.YES
_l_(5014)

exit(aux)
