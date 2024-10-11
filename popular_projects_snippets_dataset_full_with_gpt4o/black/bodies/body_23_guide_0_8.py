import typing # pragma: no cover
from typing import Any # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def any_open_brackets(self) -> bool: # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __call__(self) -> None: # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class SelfType: # pragma: no cover
    current_line: Any # pragma: no cover
    def line(self) -> None: # pragma: no cover
        pass # pragma: no cover
    def visit_default(self, leaf: Any) -> None: # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = SelfType() # pragma: no cover
self.current_line = type('Mock', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover

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
