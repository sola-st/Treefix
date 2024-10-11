from typing import List, Optional, Any # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self, type: str):# pragma: no cover
        self.type = type# pragma: no cover
    children = []# pragma: no cover
# pragma: no cover
gexp = Mock('testlist_gexp')# pragma: no cover
# pragma: no cover
node = Mock('atom')# pragma: no cover
# pragma: no cover
class Syms:# pragma: no cover
    atom = 'atom'# pragma: no cover
    testlist_gexp = 'testlist_gexp'# pragma: no cover
    namedexpr_test = 'namedexpr_test'# pragma: no cover
# pragma: no cover
syms = Syms()# pragma: no cover
# pragma: no cover
def unwrap_singleton_parenthesis(node: Mock) -> Optional[Mock]:# pragma: no cover
    return node if node.type == 'testlist_gexp' else None # pragma: no cover

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
