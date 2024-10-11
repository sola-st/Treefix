from typing import Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class Node: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class SelfType: # pragma: no cover
    def line(self, increment: int) -> Any: # pragma: no cover
        return 'Indented line' # pragma: no cover
 # pragma: no cover
    def visit_default(self, node: Node) -> Any: # pragma: no cover
        return 'Visited node' # pragma: no cover
 # pragma: no cover
self = SelfType() # pragma: no cover
node = Node() # pragma: no cover

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
