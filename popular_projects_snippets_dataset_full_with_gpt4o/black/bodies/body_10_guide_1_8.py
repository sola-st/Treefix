class Mock(object): # pragma: no cover
    def line(self, increment): # pragma: no cover
        return f'Line with increment {increment}' # pragma: no cover
 # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        return 'Visited default node' # pragma: no cover
 # pragma: no cover
# Initialize the instance and node # pragma: no cover
self = Mock() # pragma: no cover
node = None # pragma: no cover

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
