from typing import List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
Leaf = type('Leaf', (object,), {'__call__': lambda self, type, value: Leaf(type, value)}) # pragma: no cover
 # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, type: int, children: List): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
class MockToken: # pragma: no cover
    DOT = 1 # pragma: no cover
 # pragma: no cover
class MockSyms: # pragma: no cover
    simple_stmt = 2 # pragma: no cover
    atom = 3 # pragma: no cover
Node = MockNode # pragma: no cover
syms = MockSyms # pragma: no cover
token = MockToken # pragma: no cover

from typing import List # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class Node:# pragma: no cover
    pass
class Leaf:# pragma: no cover
    def __init__(self, token_type, value: str):# pragma: no cover
        self.token_type = token_type# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
    def __eq__(self, other):# pragma: no cover
        return isinstance(other, Leaf) and self.token_type == other.token_type and self.value == other.value # pragma: no cover
syms = SimpleNamespace(simple_stmt=1, atom=2) # pragma: no cover
token = SimpleNamespace(DOT=3) # pragma: no cover

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
