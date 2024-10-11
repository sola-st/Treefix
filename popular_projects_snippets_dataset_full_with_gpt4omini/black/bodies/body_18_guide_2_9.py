import token # pragma: no cover
from typing import List # pragma: no cover

class Node:  # Mock class to simulate AST nodes# pragma: no cover
    def __init__(self, children: List, node_type: str):# pragma: no cover
        self.children = children# pragma: no cover
        self.type = node_type # pragma: no cover
class MockVisitor:  # Mock class for self with the required methods# pragma: no cover
    def line(self):# pragma: no cover
        return 'some line'# pragma: no cover
    # pragma: no cover
    def visit(self, child: Node):# pragma: no cover
        return 'visited' # pragma: no cover
self = MockVisitor() # pragma: no cover
async_child = Node([], token.ASYNC)  # Create a mock async child node# pragma: no cover
internal_stmt_child = Node([], 'internal_stmt')  # Create a mock internal statement node# pragma: no cover
node = Node([async_child, internal_stmt_child], 'root')  # Create the root node with children # pragma: no cover

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
