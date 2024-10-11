from typing import Callable # pragma: no cover

class Mock: pass # pragma: no cover
node = 'mocked_node' # pragma: no cover

from typing import Any # pragma: no cover

class Context:# pragma: no cover
    def line(self, x: int) -> int:# pragma: no cover
        return x + 1# pragma: no cover
# pragma: no cover
    def visit_default(self, node: Any) -> str:# pragma: no cover
        return 'visited ' + str(node)# pragma: no cover
# pragma: no cover
self = Context() # pragma: no cover
node = 'mock_node' # pragma: no cover

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
