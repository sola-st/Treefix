import token # pragma: no cover
from typing import List # pragma: no cover

class MockNode:  # Mock class for a node containing children# pragma: no cover
    def __init__(self, children: List):# pragma: no cover
        self.children = children# pragma: no cover
        self.type = '' # pragma: no cover
class MockSelf:  # Mock class for self with required methods# pragma: no cover
    def line(self):# pragma: no cover
        return 42  # Returns an integer for the line method# pragma: no cover
    def visit(self, node):# pragma: no cover
        return 'visited'  # Returns a string for visited nodes # pragma: no cover
self = MockSelf() # pragma: no cover
children = [MockNode(children=[]), MockNode(children=[])] # pragma: no cover
node = MockNode(children=children) # pragma: no cover
async_node = MockNode(children=[])  # Mock async node # pragma: no cover
async_node.type = token.ASYNC # pragma: no cover
children[0] = async_node # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Visit `async def`, `async for`, `async with`."""
aux = self.line()
_l_(8675)
exit(aux)

children = iter(node.children)
_l_(8676)
for child in children:
    _l_(8680)

    aux = self.visit(child)
    _l_(8677)
    exit(aux)

    if child.type == token.ASYNC or child.type == STANDALONE_COMMENT:
        _l_(8679)

        # STANDALONE_COMMENT happens when `# fmt: skip` is applied on the async
        # line.
        break
        _l_(8678)

internal_stmt = next(children)
_l_(8681)
for child in internal_stmt.children:
    _l_(8683)

    aux = self.visit(child)
    _l_(8682)
    exit(aux)
