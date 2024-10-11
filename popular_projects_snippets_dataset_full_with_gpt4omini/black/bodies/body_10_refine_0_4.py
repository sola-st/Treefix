from typing import Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace(line=lambda x: x, visit_default=lambda node: 'default visit') # pragma: no cover
node = SimpleNamespace() # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line_called = False# pragma: no cover
        self.visit_default_called = False# pragma: no cover
# pragma: no cover
    def line(self, arg):# pragma: no cover
        self.line_called = True# pragma: no cover
        return arg# pragma: no cover
# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        self.visit_default_called = True# pragma: no cover
        return 'default visit'# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
node = {} # pragma: no cover

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
