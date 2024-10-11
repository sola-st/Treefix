from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.current_line = SimpleNamespace(bracket_tracker=SimpleNamespace(any_open_brackets=lambda: False)) # pragma: no cover
self.line = lambda: 'example line' # pragma: no cover
self.visit_default = lambda leaf: 'default visit result' # pragma: no cover
leaf = 'example leaf' # pragma: no cover

class BracketTrackerMock:# pragma: no cover
    def any_open_brackets(self):# pragma: no cover
        return False# pragma: no cover
# pragma: no cover
class CurrentLineMock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = BracketTrackerMock()# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.current_line = CurrentLineMock()# pragma: no cover
    def line(self):# pragma: no cover
        return 'example line'# pragma: no cover
    def visit_default(self, leaf):# pragma: no cover
        return 'default visit result'# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
leaf = 'example leaf' # pragma: no cover

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
