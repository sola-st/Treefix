from typing import NamedTuple, List # pragma: no cover

class MockNode(NamedTuple):# pragma: no cover
    type: int# pragma: no cover
    children: List['MockNode'] # pragma: no cover
class MockSyms(NamedTuple):# pragma: no cover
    atom: int# pragma: no cover
    testlist_gexp: int# pragma: no cover
    namedexpr_test: int # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    return node if len(node.children) == 1 else None # pragma: no cover
node = MockNode(type=1, children=[MockNode(type=3, children=[]), MockNode(type=2, children=[])]) # pragma: no cover
syms = MockSyms(atom=1, testlist_gexp=2, namedexpr_test=3) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` holds a tuple that contains a walrus operator."""
if node.type != syms.atom:
    _l_(17730)

    aux = False
    _l_(17729)
    exit(aux)
gexp = unwrap_singleton_parenthesis(node)
_l_(17731)
if gexp is None or gexp.type != syms.testlist_gexp:
    _l_(17733)

    aux = False
    _l_(17732)
    exit(aux)
aux = any(child.type == syms.namedexpr_test for child in gexp.children)
_l_(17734)

exit(aux)
