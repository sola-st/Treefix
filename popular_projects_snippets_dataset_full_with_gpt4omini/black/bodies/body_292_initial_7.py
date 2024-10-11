from typing import Optional, List # pragma: no cover

class Mock:# pragma: no cover
    pass # pragma: no cover
class Syms:# pragma: no cover
    atom = 'atom'# pragma: no cover
    testlist_gexp = 'testlist_gexp'# pragma: no cover
    namedexpr_test = 'namedexpr_test' # pragma: no cover
syms = Syms() # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    return node if isinstance(node, tuple) and len(node) == 1 else None # pragma: no cover
node = Mock()# pragma: no cover
node.type = syms.atom# pragma: no cover
node.children = [Mock(), Mock()]# pragma: no cover
node.children[0].type = syms.namedexpr_test# pragma: no cover
node.children[1].type = 'other_type' # pragma: no cover

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
