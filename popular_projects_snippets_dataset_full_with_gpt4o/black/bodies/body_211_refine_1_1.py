text = '1.0' # pragma: no cover

text = 'example.5' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/numerics.py
from l3.Runtime import _l_
"""Formats a float string like "1.0"."""
if "." not in text:
    _l_(17927)

    aux = text
    _l_(17926)
    exit(aux)

before, after = text.split(".")
_l_(17928)
aux = f"{before or 0}.{after or 0}"
_l_(17929)
exit(aux)
