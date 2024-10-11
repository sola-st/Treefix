from typing import List, Optional, Any # pragma: no cover

class Mock: pass# pragma: no cover
syms = Mock()# pragma: no cover
syms.atom = 'atom'# pragma: no cover
syms.testlist_gexp = 'testlist_gexp'# pragma: no cover
syms.namedexpr_test = 'namedexpr_test' # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, node_type):# pragma: no cover
        self.type = node_type# pragma: no cover
# pragma: no cover
node = Node(syms.atom) # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    return Node(syms.testlist_gexp) if node.type == syms.atom else None # pragma: no cover

from typing import List, Optional, Any # pragma: no cover

class Mock: pass# pragma: no cover
syms = Mock()# pragma: no cover
syms.atom = 'atom'# pragma: no cover
syms.testlist_gexp = 'testlist_gexp'# pragma: no cover
syms.namedexpr_test = 'namedexpr_test' # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, node_type, children=None):# pragma: no cover
        self.type = node_type# pragma: no cover
        self.children = children if children is not None else []# pragma: no cover
# pragma: no cover
node = Node(syms.atom) # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    return Node(syms.testlist_gexp, [Node(syms.namedexpr_test)]) if node.type == syms.atom else None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` holds a tuple that contains a walrus operator."""
if node.type != syms.atom:
    _l_(6236)

    aux = False
    _l_(6235)
    exit(aux)
gexp = unwrap_singleton_parenthesis(node)
_l_(6237)
if gexp is None or gexp.type != syms.testlist_gexp:
    _l_(6239)

    aux = False
    _l_(6238)
    exit(aux)
aux = any(child.type == syms.namedexpr_test for child in gexp.children)
_l_(6240)

exit(aux)
