from typing import List, Iterator, Any # pragma: no cover
import token # pragma: no cover

class Mock:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.line = lambda: None # pragma: no cover
        self.visit = lambda x: None # pragma: no cover
self = Mock() # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, children: List[Any]): # pragma: no cover
        self.children = children # pragma: no cover
node = Node(children=[]) # pragma: no cover
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
