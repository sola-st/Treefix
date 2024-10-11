from typing import List, Any # pragma: no cover
from lib2to3.pytree import Leaf # pragma: no cover
from lib2to3.pytree import Node # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3.pgen2.grammar import Grammar # pragma: no cover

class EllipsisSymbol: # pragma: no cover
    simple_stmt = 1 # pragma: no cover
    atom = 2 # pragma: no cover
 # pragma: no cover
syms = EllipsisSymbol() # pragma: no cover

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
