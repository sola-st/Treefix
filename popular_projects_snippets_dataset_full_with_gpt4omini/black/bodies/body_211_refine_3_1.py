text = '1.0' # pragma: no cover

text = '1.0' # pragma: no cover
exit = lambda msg: print(msg) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/numerics.py
from l3.Runtime import _l_
"""Formats a float string like "1.0"."""
if "." not in text:
    _l_(6431)

    aux = text
    _l_(6430)
    exit(aux)

before, after = text.split(".")
_l_(6432)
aux = f"{before or 0}.{after or 0}"
_l_(6433)
exit(aux)
