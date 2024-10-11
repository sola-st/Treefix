from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Mock:# pragma: no cover
    def line(self):# pragma: no cover
        return 'Exit called'# pragma: no cover
# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'Visited: ' + str(child)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List[Any]):# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
node = Node(children=[]) # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Mock:# pragma: no cover
    def line(self):# pragma: no cover
        print('Exit called')# pragma: no cover
# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'Visited: ' + str(child)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List[Any]):# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
node = Node(children=[]) # pragma: no cover
class Child:# pragma: no cover
    def __init__(self, type_value):# pragma: no cover
        self.type = type_value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Child(type={self.type})'# pragma: no cover
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
