leaf = object() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'current_line': type('Mock', (object,), { # pragma: no cover
        'bracket_tracker': type('Mock', (object,), { # pragma: no cover
            'any_open_brackets': lambda: False # pragma: no cover
        })() # pragma: no cover
    })(), # pragma: no cover
    'line': lambda: 0, # pragma: no cover
    'visit_default': lambda x: 1 # pragma: no cover
})() # pragma: no cover

from typing import Any # pragma: no cover

leaf = 'example_leaf' # pragma: no cover
class BracketTrackerMock: # pragma: no cover
    def any_open_brackets(self) -> bool: # pragma: no cover
        return False # pragma: no cover
class CurrentLineMock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = BracketTrackerMock() # pragma: no cover
class SelfMock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.current_line = CurrentLineMock() # pragma: no cover
    def line(self) -> int: # pragma: no cover
        return 0 # pragma: no cover
    def visit_default(self, leaf: Any) -> int: # pragma: no cover
        return 1 # pragma: no cover
self = SelfMock() # pragma: no cover

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
