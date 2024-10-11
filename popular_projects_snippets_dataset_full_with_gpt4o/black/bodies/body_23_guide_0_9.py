from typing import Any # pragma: no cover
class Leaf: pass # pragma: no cover

self = type('Mock', (object,), {'current_line': type('MockLine', (object,), {'bracket_tracker': type('MockBracket', (object,), {'any_open_brackets': lambda self: False})()})()})() # pragma: no cover
self.line = lambda: 'Mocked aux value' # pragma: no cover
self.visit_default = lambda leaf: 'Visited leaf' # pragma: no cover
leaf = Leaf() # pragma: no cover

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
