from collections import namedtuple # pragma: no cover
import token # pragma: no cover

self = type('Mock', (object,), { 'line': lambda self: 'Mock line called', 'visit': lambda self, n: 'Mock visit called' })() # pragma: no cover
MockNode = namedtuple('MockNode', ['children']) # pragma: no cover
node = MockNode(children=[type('MockChild', (object,), {'type': token.ASYNC})(), type('MockChild', (object,), {'type': 'OTHER'})(), MockNode(children=[])]) # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover

from collections import namedtuple # pragma: no cover
import token # pragma: no cover

MockNode = namedtuple('MockNode', ['children']) # pragma: no cover
node = MockNode(children=[type('MockChild', (object,), {'type': token.ASYNC, 'children': []})(), type('MockChild', (object,), {'type': 'OTHER', 'children': []})()]) # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover

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
