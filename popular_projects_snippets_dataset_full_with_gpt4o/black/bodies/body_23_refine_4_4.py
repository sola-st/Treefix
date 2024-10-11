from typing import Any # pragma: no cover

leaf = 'leaf_value' # pragma: no cover
MockCurrentLine = type('MockCurrentLine', (object,), {'bracket_tracker': type('MockBracketTracker', (object,), {'any_open_brackets': lambda self: False})()}) # pragma: no cover
self = type('MockSelf', (object,), {'current_line': MockCurrentLine(), 'line': lambda self: 1, 'visit_default': lambda self, leaf: 2})() # pragma: no cover

leaf = 'dummy_leaf' # pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'any_open_brackets': lambda self: False}) # pragma: no cover
current_line = type('CurrentLine', (object,), {'bracket_tracker': BracketTracker()}) # pragma: no cover
self = type('Self', (object,), {'current_line': current_line(), 'line': lambda self: 'Exiting line', 'visit_default': lambda self, leaf: 'Default visit'})() # pragma: no cover

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
