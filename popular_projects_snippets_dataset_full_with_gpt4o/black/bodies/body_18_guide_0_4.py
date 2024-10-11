import token # pragma: no cover

STANDALONE_COMMENT = 999 # pragma: no cover
class Node: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.children = [ChildNode(), ChildNode(ASYNC=True), ChildNode()] # pragma: no cover
self = type('Mock', (object,), {'line': lambda: 0, 'visit': lambda x: None})() # pragma: no cover
class ChildNode: # pragma: no cover
    def __init__(self, ASYNC=False): # pragma: no cover
        if ASYNC: # pragma: no cover
            self.type = token.ASYNC # pragma: no cover
        else: # pragma: no cover
            self.type = None # pragma: no cover
self.line = lambda: 0 # pragma: no cover
node = Node() # pragma: no cover

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
