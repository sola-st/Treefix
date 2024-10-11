import sys # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def any_open_brackets(self): # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
class MockCurrentLine: # pragma: no cover
    bracket_tracker = MockBracketTracker() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    current_line = MockCurrentLine() # pragma: no cover
    def line(self): # pragma: no cover
        return 'line_value' # pragma: no cover
    def visit_default(self, leaf): # pragma: no cover
        return 'visit_default_value' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
leaf = type('Mock', (object,), {})() # pragma: no cover
 # pragma: no cover
exit = sys.exit # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if not self.current_line.bracket_tracker.any_open_brackets():
    _l_(16729)

    aux = self.line()
    _l_(16728)
    exit(aux)
aux = self.visit_default(leaf)
_l_(16730)
exit(aux)
