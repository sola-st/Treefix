from typing import Any # pragma: no cover
import sys # pragma: no cover
import symtable # pragma: no cover

node = type('MockNode', (object,), {'type': 'some_other_type', 'children': []})() # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 'atom', 'testlist_gexp': 'testlist_gexp', 'namedexpr_test': 'namedexpr_test'})() # pragma: no cover
def unwrap_singleton_parenthesis(node): return None # pragma: no cover

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
