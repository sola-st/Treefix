from typing import Any # pragma: no cover
from functools import partial # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Node: # pragma: no cover
    type: Any # pragma: no cover
    children: list # pragma: no cover
 # pragma: no cover
class SimpleStatementSymbols: # pragma: no cover
    simple_stmt = 'simple_stmt' # pragma: no cover
 # pragma: no cover
syms = SimpleStatementSymbols() # pragma: no cover
 # pragma: no cover
token = type('MockToken', (object,), {'DOT': 'DOT'}) # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, token_type, value): # pragma: no cover
        self.token_type = token_type # pragma: no cover
        self.value = value # pragma: no cover
    def __eq__(self, other): # pragma: no cover
        return self.token_type == other.token_type and self.value == other.value # pragma: no cover
 # pragma: no cover
# Example node object to trigger an uncovered path # pragma: no cover
node = Node(type='simple_stmt', children=[]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` is a simple statement containing an ellipsis."""
if not isinstance(node, Node) or node.type != syms.simple_stmt:
    _l_(19684)

    aux = False
    _l_(19683)
    exit(aux)

if len(node.children) != 2:
    _l_(19686)

    aux = False
    _l_(19685)
    exit(aux)

child = node.children[0]
_l_(19687)
aux = (
    child.type == syms.atom
    and len(child.children) == 3
    and all(leaf == Leaf(token.DOT, ".") for leaf in child.children)
)
_l_(19688)
exit(aux)
