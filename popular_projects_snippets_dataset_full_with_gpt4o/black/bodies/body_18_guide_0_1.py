from __future__ import annotations # pragma: no cover
import token # pragma: no cover

aux = None # pragma: no cover
exit = lambda x: None # pragma: no cover
node = type('MockNode', (object,), {'children': [type('Child', (object,), {'type': token.ASYNC, 'children': []})]})() # pragma: no cover
self = type('MockSelf', (object,), {'line': lambda: 'line_content', 'visit': lambda x: 'visited'})() # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover

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
