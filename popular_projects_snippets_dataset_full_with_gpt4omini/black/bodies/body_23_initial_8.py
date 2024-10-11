import numpy as np # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def any_open_brackets(self):# pragma: no cover
        return False # pragma: no cover
class MockLine:# pragma: no cover
    def bracket_tracker(self):# pragma: no cover
        return MockBracketTracker() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.current_line = MockLine()# pragma: no cover
    def line(self):# pragma: no cover
        return 0# pragma: no cover
    def visit_default(self, leaf):# pragma: no cover
        return f'Visited {leaf}' # pragma: no cover
self = MockSelf() # pragma: no cover
leaf = 'example_leaf' # pragma: no cover

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
