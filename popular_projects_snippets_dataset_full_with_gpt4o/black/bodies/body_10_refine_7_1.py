import ast # pragma: no cover

self = type('Mock', (object,), {'line': lambda self, x: f'Line {x} incremented', 'visit_default': lambda self, node: 'Visited default'})() # pragma: no cover
node = ast.AST() # pragma: no cover

self = type('Mock', (object,), {'line': lambda self, x: None, 'visit_default': lambda self, node: None})() # pragma: no cover
node = type('Node', (object,), {})() # pragma: no cover

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
