class MockBlinker: # pragma: no cover
    pass # pragma: no cover
blinker = MockBlinker() # pragma: no cover
if not hasattr(blinker, 'Signal'): # pragma: no cover
    pass

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/signals.py
from l3.Runtime import _l_
raise RuntimeError(
    "Signalling support is unavailable because the blinker"
    " library is not installed."
) from None
_l_(16590)
