import ast # pragma: no cover

class MockVisitor: # pragma: no cover
    def line(self, increment): # pragma: no cover
        print(f"Indentation level increased by {increment}") # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        print("Visiting default node") # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
node = ast.parse('') # pragma: no cover
self = MockVisitor() # pragma: no cover

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
