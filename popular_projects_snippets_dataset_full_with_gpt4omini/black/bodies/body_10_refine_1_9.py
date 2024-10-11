import typing # pragma: no cover

class MockNode:# pragma: no cover
    pass# pragma: no cover
node = MockNode() # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line = lambda x: x# pragma: no cover
        self.visit_default = lambda n: n# pragma: no cover
self = Mock() # pragma: no cover

class MockNode:# pragma: no cover
    pass# pragma: no cover
node = MockNode() # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line = lambda x: x + 1# pragma: no cover
        self.visit_default = lambda n: f'Visited: {n}'# pragma: no cover
self = Mock() # pragma: no cover

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
