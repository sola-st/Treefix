import token # pragma: no cover

self = type('MockSelf', (object,), {'tree_depth': 0, 'visit': lambda self, child: None})() # pragma: no cover
node = type('MockNode', (object,), {'type': 'TYPE', 'children': [], 'prefix': '', 'value': 'value'})() # pragma: no cover
Node = type('Node', (object,), {}) # pragma: no cover
type_repr = lambda _type: str(_type) # pragma: no cover
out = lambda *args, **kwargs: print(' '.join(map(str, args))) # pragma: no cover
token.tok_name = {node.type: 'MOCK_TYPE'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/debug.py
from l3.Runtime import _l_
indent = " " * (2 * self.tree_depth)
_l_(19281)
if isinstance(node, Node):
    _l_(19294)

    _type = type_repr(node.type)
    _l_(19282)
    out(f"{indent}{_type}", fg="yellow")
    _l_(19283)
    self.tree_depth += 1
    _l_(19284)
    for child in node.children:
        _l_(19286)

        aux = self.visit(child)
        _l_(19285)
        exit(aux)

    self.tree_depth -= 1
    _l_(19287)
    out(f"{indent}/{_type}", fg="yellow", bold=False)
    _l_(19288)
else:
    _type = token.tok_name.get(node.type, str(node.type))
    _l_(19289)
    out(f"{indent}{_type}", fg="blue", nl=False)
    _l_(19290)
    if node.prefix:
        _l_(19292)

        # We don't have to handle prefixes for `Node` objects since
        # that delegates to the first child anyway.
        out(f" {node.prefix!r}", fg="green", bold=False, nl=False)
        _l_(19291)
    out(f" {node.value!r}", fg="blue", bold=False)
    _l_(19293)
