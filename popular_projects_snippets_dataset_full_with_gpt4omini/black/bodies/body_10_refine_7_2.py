class Mock: pass # pragma: no cover

self = type('Mock', (object,), {'line': lambda x: x, 'visit_default': lambda x: x})() # pragma: no cover
node = type('MockNode', (object,), {})() # pragma: no cover

class Mock: pass # pragma: no cover

self = type('Mock', (object,), {'line': lambda self, x: x, 'visit_default': lambda self, node: node})() # pragma: no cover
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
