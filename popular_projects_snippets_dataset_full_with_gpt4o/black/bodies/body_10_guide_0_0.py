class MockSelf(type('Mock', (object,), {'line': lambda self, x: 'line called with ' + str(x), 'visit_default': lambda self, node: 'visit_default called'})): pass # pragma: no cover
self = MockSelf() # pragma: no cover
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
