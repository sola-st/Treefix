from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.current_line = SimpleNamespace(bracket_tracker=SimpleNamespace(any_open_brackets=lambda: False)) # pragma: no cover
self.line = lambda: 'example line' # pragma: no cover
self.visit_default = lambda leaf: 'default visit result' # pragma: no cover
leaf = 'example leaf' # pragma: no cover

leaf = object() # pragma: no cover
MockBracketTracker = type('MockBracketTracker', (object,), {'any_open_brackets': (lambda self: False)}) # pragma: no cover
MockCurrentLine = type('MockCurrentLine', (object,), {'bracket_tracker': MockBracketTracker()}) # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'current_line': MockCurrentLine(), # pragma: no cover
    'line': lambda self: 'Exiting due to no open brackets', # pragma: no cover
    'visit_default': lambda self, leaf: 'Default visit handling' # pragma: no cover
})() # pragma: no cover

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
