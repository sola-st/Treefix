blinker_installed = False # pragma: no cover
if not blinker_installed: # pragma: no cover
    pass

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/signals.py
from l3.Runtime import _l_
raise RuntimeError(
    "Signalling support is unavailable because the blinker"
    " library is not installed."
) from None
_l_(16590)
