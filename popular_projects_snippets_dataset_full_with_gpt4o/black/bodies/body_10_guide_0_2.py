from typing import Any # pragma: no cover
class Node: pass # pragma: no cover

class MockSelf: # pragma: no cover
    def line(self, arg: int) -> str: # pragma: no cover
        return 'Line with indentation {}'.format(arg) # pragma: no cover
 # pragma: no cover
    def visit_default(self, node: Node) -> str: # pragma: no cover
        return 'Default visit for node' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
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
