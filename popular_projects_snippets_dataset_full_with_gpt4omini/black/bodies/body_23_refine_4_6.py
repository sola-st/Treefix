from unittest.mock import MagicMock # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MagicMock() # pragma: no cover
self = type('Mock', (object,), {'current_line': MockLine(), 'line': lambda: 1, 'visit_default': lambda x: 'default'})() # pragma: no cover
leaf = 'leaf_node' # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MagicMock() # pragma: no cover
self = type('Mock', (object,), {'current_line': MockLine(), 'line': lambda: 'exiting line', 'visit_default': lambda leaf: 'default response'})() # pragma: no cover
leaf = 'test_leaf' # pragma: no cover

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
