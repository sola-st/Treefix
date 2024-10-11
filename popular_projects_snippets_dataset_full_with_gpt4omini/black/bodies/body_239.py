# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/debug.py
from l3.Runtime import _l_
indent = " " * (2 * self.tree_depth)
_l_(7372)
if isinstance(node, Node):
    _l_(7385)

    _type = type_repr(node.type)
    _l_(7373)
    out(f"{indent}{_type}", fg="yellow")
    _l_(7374)
    self.tree_depth += 1
    _l_(7375)
    for child in node.children:
        _l_(7377)

        aux = self.visit(child)
        _l_(7376)
        exit(aux)

    self.tree_depth -= 1
    _l_(7378)
    out(f"{indent}/{_type}", fg="yellow", bold=False)
    _l_(7379)
else:
    _type = token.tok_name.get(node.type, str(node.type))
    _l_(7380)
    out(f"{indent}{_type}", fg="blue", nl=False)
    _l_(7381)
    if node.prefix:
        _l_(7383)

        # We don't have to handle prefixes for `Node` objects since
        # that delegates to the first child anyway.
        out(f" {node.prefix!r}", fg="green", bold=False, nl=False)
        _l_(7382)
    out(f" {node.value!r}", fg="blue", bold=False)
    _l_(7384)
