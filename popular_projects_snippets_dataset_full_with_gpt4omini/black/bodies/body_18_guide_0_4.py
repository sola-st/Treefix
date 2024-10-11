import token # pragma: no cover
class Node: pass # pragma: no cover
class Mock: pass # pragma: no cover

self = type('Mock', (), {'line': lambda self: 'line called', 'visit': lambda self, child: 'visited child'})() # pragma: no cover
node = Node() # pragma: no cover
node.children = [Node(), Node()] # pragma: no cover
node.children[0].type = token.ASYNC # pragma: no cover
node.children[0].children = [Node()] # pragma: no cover
node.children[1].children = [] # pragma: no cover

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
