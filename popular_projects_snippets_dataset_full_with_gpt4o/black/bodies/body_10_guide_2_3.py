from typing import Any # pragma: no cover
import sys # pragma: no cover

class MockVisitor: # pragma: no cover
    def line(self, increment: int) -> str: # pragma: no cover
        return 'line with indent level ' + str(increment) # pragma: no cover
 # pragma: no cover
    def visit_default(self, node: Any) -> str: # pragma: no cover
        return 'default visit for node' # pragma: no cover
 # pragma: no cover
self = MockVisitor() # pragma: no cover
node = 'mock_node' # pragma: no cover
exit = sys.exit # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Increase indentation level, maybe yield a line."""
aux = self.line(+1)
_l_(17801)
# In blib2to3 INDENT never holds comments.
exit(aux)
aux = self.visit_default(node)
_l_(17802)
exit(aux)
