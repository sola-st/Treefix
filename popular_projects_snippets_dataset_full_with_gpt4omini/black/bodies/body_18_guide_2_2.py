import token # pragma: no cover
from typing import List # pragma: no cover

class MockNode:  # Mock class representing a node# pragma: no cover
    def __init__(self, children: List, type: str):# pragma: no cover
        self.children = children# pragma: no cover
        self.type = type # pragma: no cover
class MockSelf:  # Mock class to replace self# pragma: no cover
    def line(self):# pragma: no cover
        return 'called line'# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'visited child' # pragma: no cover
self = MockSelf() # pragma: no cover
async_child = MockNode([], token.ASYNC) # pragma: no cover
normal_child = MockNode([], 'statement') # pragma: no cover
node = MockNode([async_child, normal_child], 'root') # pragma: no cover

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
