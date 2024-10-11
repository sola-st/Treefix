class MockNode: pass # pragma: no cover
class MockSelf: # pragma: no cover
    def line(self, increment): # pragma: no cover
        return f'Line with increment {increment}' # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        return f'Visited {node}' # pragma: no cover

self = MockSelf() # pragma: no cover
node = MockNode() # pragma: no cover

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
