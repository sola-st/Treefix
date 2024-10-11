Mock = type('Mock', (object,), {'line': lambda self, x: 'line_with_indent', 'visit_default': lambda self, node: 'default_visit'}) # pragma: no cover
self = Mock() # pragma: no cover
node = object() # pragma: no cover

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
