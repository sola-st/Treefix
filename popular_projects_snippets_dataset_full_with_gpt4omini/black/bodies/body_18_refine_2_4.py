from typing import List, Iterable # pragma: no cover
import token # pragma: no cover

class Mock:# pragma: no cover
    def line(self):# pragma: no cover
        return 'Exiting line'# pragma: no cover
    def visit(self, child):# pragma: no cover
        return f'Visited {child.type}' # pragma: no cover
node = Mock() # pragma: no cover
node.children = [Mock()] * 2# pragma: no cover
node.children[0].type = token.ASYNC# pragma: no cover
node.children[1].type = 'COMMENT' # pragma: no cover
token.ASYNC = 'async' # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
self = Mock() # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Mock:# pragma: no cover
    def line(self):# pragma: no cover
        print('Exiting line')# pragma: no cover
    def visit(self, child):# pragma: no cover
        return f'Visited {child.type}' # pragma: no cover
self = Mock() # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List[Any]):# pragma: no cover
        self.children = children# pragma: no cover
    def __iter__(self):# pragma: no cover
        return iter(self.children)# pragma: no cover
node = Node(children=[]) # pragma: no cover
node.children = [Mock() for _ in range(2)]# pragma: no cover
node.children[0].type = token.ASYNC# pragma: no cover
node.children[1].type = 'COMMENT' # pragma: no cover
token.ASYNC = 'async' # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover

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
