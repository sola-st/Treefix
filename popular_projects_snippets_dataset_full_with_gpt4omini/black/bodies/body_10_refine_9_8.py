from typing import Any, Optional # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line = lambda x: x# pragma: no cover
    def visit_default(self, node: Any) -> Optional[Any]:# pragma: no cover
        return 'default_visit_result'# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
node = 'example_node' # pragma: no cover

class Mock:# pragma: no cover
    def line(self, x):# pragma: no cover
        return x + 1# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'Visited: ' + str(node)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
node = 'example_node' # pragma: no cover

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
