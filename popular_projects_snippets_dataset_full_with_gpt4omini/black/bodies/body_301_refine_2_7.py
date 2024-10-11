from lib2to3.pgen2.token import DOT # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover

class syms:# pragma: no cover
    simple_stmt = 'simple_stmt'# pragma: no cover
    atom = 'atom' # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
Leaf = Leaf # pragma: no cover

from lib2to3.pgen2.token import DOT # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` is a simple statement containing an ellipsis."""
if not isinstance(node, Node) or node.type != syms.simple_stmt:
    _l_(7917)

    aux = False
    _l_(7916)
    exit(aux)

if len(node.children) != 2:
    _l_(7919)

    aux = False
    _l_(7918)
    exit(aux)

child = node.children[0]
_l_(7920)
aux = (
    child.type == syms.atom
    and len(child.children) == 3
    and all(leaf == Leaf(token.DOT, ".") for leaf in child.children)
)
_l_(7921)
exit(aux)
