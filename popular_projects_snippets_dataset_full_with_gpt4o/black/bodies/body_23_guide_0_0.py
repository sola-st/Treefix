from typing import Any # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def any_open_brackets(self) -> bool:# pragma: no cover
        return False # pragma: no cover
class MockLeaf:# pragma: no cover
    pass # pragma: no cover
class MockLine:# pragma: no cover
    def bracket_tracker(self) -> MockBracketTracker:# pragma: no cover
        return MockBracketTracker() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self) -> None:# pragma: no cover
        self.current_line = MockLine()# pragma: no cover
    def line(self) -> Any:# pragma: no cover
        return 'line_output'# pragma: no cover
    def visit_default(self, leaf: MockLeaf) -> Any:# pragma: no cover
        return 'visit_output' # pragma: no cover
self = MockSelf() # pragma: no cover
leaf = MockLeaf() # pragma: no cover

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
