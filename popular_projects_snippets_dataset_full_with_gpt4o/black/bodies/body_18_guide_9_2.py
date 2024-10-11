import token # pragma: no cover

class MockVisitor: # pragma: no cover
    def line(self): # pragma: no cover
        return 'line_result' # pragma: no cover
    def visit(self, child): # pragma: no cover
        return 'visit_result' # pragma: no cover
 # pragma: no cover
class MockChild: # pragma: no cover
    def __init__(self, type_, children=None): # pragma: no cover
        self.type = type_ # pragma: no cover
        self.children = children if children else [] # pragma: no cover
 # pragma: no cover
first_child = MockChild(token.ASYNC) # pragma: no cover
internal_child = MockChild('internal_child') # pragma: no cover
internal_stmt = MockChild('internal_stmt', [internal_child]) # pragma: no cover
node = type('MockNode', (object,), {'children': [first_child, internal_stmt]})() # pragma: no cover
self = MockVisitor() # pragma: no cover
STANDALONE_COMMENT = token.ASYNC # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Visit `async def`, `async for`, `async with`."""
aux = self.line()
_l_(20224)
exit(aux)

children = iter(node.children)
_l_(20225)
for child in children:
    _l_(20229)

    aux = self.visit(child)
    _l_(20226)
    exit(aux)

    if child.type == token.ASYNC or child.type == STANDALONE_COMMENT:
        _l_(20228)

        # STANDALONE_COMMENT happens when `# fmt: skip` is applied on the async
        # line.
        break
        _l_(20227)

internal_stmt = next(children)
_l_(20230)
for child in internal_stmt.children:
    _l_(20232)

    aux = self.visit(child)
    _l_(20231)
    exit(aux)
