from typing import Any, Callable # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line = lambda x: x * 2# pragma: no cover
        self.visit_default = lambda node: node + 1# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
node = 1 # pragma: no cover

from typing import Any # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line = self.line_method# pragma: no cover
        self.visit_default = self.visit_default_method# pragma: no cover
# pragma: no cover
    def line_method(self, increment: int) -> int:# pragma: no cover
        return 2 + increment# pragma: no cover
# pragma: no cover
    def visit_default_method(self, node: Any) -> str:# pragma: no cover
        return f'Visited node: {node}'# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
node = 'Sample Node' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Increase indentation level, maybe yield a line."""
aux = self.line(+1)
_l_(5984)
# In blib2to3 INDENT never holds comments.
exit(aux)
aux = self.visit_default(node)
_l_(5985)
exit(aux)
