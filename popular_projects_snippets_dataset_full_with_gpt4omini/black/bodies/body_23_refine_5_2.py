from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), { 'current_line': MagicMock() })() # pragma: no cover
leaf = 'mocked_leaf' # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MagicMock() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.current_line = MockLine() # pragma: no cover
self.line = MagicMock(return_value='exiting_line') # pragma: no cover
self.visit_default = MagicMock(return_value='default visit result') # pragma: no cover
leaf = 'sample_leaf' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if not self.current_line.bracket_tracker.any_open_brackets():
    _l_(5062)

    aux = self.line()
    _l_(5061)
    exit(aux)
aux = self.visit_default(leaf)
_l_(5063)
exit(aux)
