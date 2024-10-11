import sys # pragma: no cover

class MockSelf: # pragma: no cover
    def line(self, indent_level: int) -> str: # pragma: no cover
        return 'line with indent level ' + str(indent_level) # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
node = 'mock_node' # pragma: no cover
exit = print # pragma: no cover

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
