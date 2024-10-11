from typing import Any # pragma: no cover

self = type('SelfMock', (object,), { # pragma: no cover
    'current_line': type('CurrentLineMock', (object,), { # pragma: no cover
        'bracket_tracker': type('BracketTrackerMock', (object,), { # pragma: no cover
            'any_open_brackets': lambda: False # pragma: no cover
        })() # pragma: no cover
    })(), # pragma: no cover
    'line': lambda: 1, # pragma: no cover
    'visit_default': lambda leaf: 0 # pragma: no cover
})() # pragma: no cover
leaf = 'example_leaf' # pragma: no cover

leaf = 'example_leaf' # pragma: no cover
BracketTrackerMock = type('BracketTrackerMock', (object,), {'any_open_brackets': lambda: False}) # pragma: no cover
CurrentLineMock = type('CurrentLineMock', (object,), {'bracket_tracker': BracketTrackerMock()}) # pragma: no cover
self = type('SelfMock', (object,), {'current_line': CurrentLineMock(), 'line': lambda: 'Line is closed', 'visit_default': lambda x: 'Default visit'})() # pragma: no cover

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
