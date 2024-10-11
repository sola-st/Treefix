try: # pragma: no cover
except ImportError: # pragma: no cover
    raise RuntimeError( # pragma: no cover
        "Signalling support is unavailable because the blinker" # pragma: no cover
        " library is not installed." # pragma: no cover
    ) from None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/signals.py
from l3.Runtime import _l_
raise RuntimeError(
    "Signalling support is unavailable because the blinker"
    " library is not installed."
) from None
_l_(16590)
