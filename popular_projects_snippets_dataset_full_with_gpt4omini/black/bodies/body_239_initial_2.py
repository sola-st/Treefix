from typing import List, Union, Callable # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, type: int, children: List['Node'], prefix: str = None, value: Union[str, int, float] = ''): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.value = value # pragma: no cover
class Token: # pragma: no cover
    tok_name = {0: 'NEWLINE', 1: 'STRING', 2: 'NUMBER'} # pragma: no cover

self = type('Mock', (object,), {'tree_depth': 0, 'visit': lambda self, x: None})() # pragma: no cover
node = Node(type=1, children=[], prefix='prefix_example', value='value_example') # pragma: no cover
Node = type('Node', (), {}) # pragma: no cover
type_repr = lambda x: 'NodeType' if x == 1 else 'UnknownType' # pragma: no cover
out = lambda msg, fg='', bold=False, nl=True: print(msg.rstrip() + ('\n' if nl else '')) # pragma: no cover
token = Token() # pragma: no cover

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
