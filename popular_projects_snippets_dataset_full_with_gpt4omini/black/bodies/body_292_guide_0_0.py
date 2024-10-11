class MockNode: # pragma: no cover
    def __init__(self, node_type, children=None): # pragma: no cover
        self.type = node_type # pragma: no cover
        self.children = children if children is not None else [] # pragma: no cover
class MockSyms: # pragma: no cover
    atom = 1 # pragma: no cover
    testlist_gexp = 2 # pragma: no cover
    namedexpr_test = 3 # pragma: no cover
syms = MockSyms() # pragma: no cover
def mock_unwrap_singleton_parenthesis(n): # pragma: no cover
    return MockNode(syms.testlist_gexp, [MockNode(syms.namedexpr_test)]) # pragma: no cover
# pragma: no cover
unwrap_singleton_parenthesis = mock_unwrap_singleton_parenthesis # pragma: no cover

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
