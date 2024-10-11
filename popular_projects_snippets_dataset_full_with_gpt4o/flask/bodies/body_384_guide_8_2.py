import sys # pragma: no cover

class MockBlinker: # pragma: no cover
    pass # pragma: no cover
mock_blinker = MockBlinker() # pragma: no cover
sys.modules['blinker'] = mock_blinker # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/signals.py
from l3.Runtime import _l_
raise RuntimeError(
    "Signalling support is unavailable because the blinker"
    " library is not installed."
) from None
_l_(16590)
