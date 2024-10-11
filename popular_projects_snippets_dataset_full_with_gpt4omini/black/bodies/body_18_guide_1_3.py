import token # pragma: no cover
from typing import List, Any # pragma: no cover

class Node:  # Mock class for a node# pragma: no cover
    def __init__(self, children: List[Any]):# pragma: no cover
        self.children = children# pragma: no cover
        self.type = '' # pragma: no cover
class MockVisitor:# pragma: no cover
    def line(self):# pragma: no cover
        return 'mock line'  # Simulate the line method# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'visited child'  # Simulate visiting a child node # pragma: no cover
self = MockVisitor() # pragma: no cover
node = Node(children=[])  # Initial node with no children to trigger path execution # pragma: no cover
child1 = Node(children=[])  # Creating a child node with async type# pragma: no cover
child1.type = token.ASYNC# pragma: no cover
node.children.append(child1)  # Add async child# pragma: no cover
 # pragma: no cover
child2 = Node(children=[])  # Creating a child node with no specific type# pragma: no cover
child2.type = 'statement'# pragma: no cover
node.children.append(child2)  # Add normal child # pragma: no cover

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
