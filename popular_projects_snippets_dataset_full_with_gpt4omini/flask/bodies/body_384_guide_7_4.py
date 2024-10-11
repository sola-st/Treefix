import sys # pragma: no cover
class MockBlinker: pass # pragma: no cover

sys.modules['blinker'] = MockBlinker() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/signals.py
from l3.Runtime import _l_
raise RuntimeError(
    "Signalling support is unavailable because the blinker"
    " library is not installed."
) from None
_l_(4885)
