import token # pragma: no cover
import sys # pragma: no cover
from typing import List, Optional # pragma: no cover

def prev_siblings_are(node, siblings): return any(child in siblings for child in node.children) # pragma: no cover

import token # pragma: no cover
from typing import List, Optional # pragma: no cover

def prev_siblings_are(parent, siblings): return True # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, children=None):# pragma: no cover
        self.children = children or []# pragma: no cover
        self.parent = None # pragma: no cover
leaf = MockNode() # pragma: no cover
leaf.parent = MockNode(children=[None, token.NEWLINE, token.INDENT, 'simple_stmt']) # pragma: no cover
token.NEWLINE = 'NEWLINE' # pragma: no cover
token.INDENT = 'INDENT' # pragma: no cover
class MockSyms:# pragma: no cover
    simple_stmt = 'simple_stmt'# pragma: no cover
    parameters = 'parameters' # pragma: no cover
syms = MockSyms() # pragma: no cover
token.COLON = 'COLON' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
if prev_siblings_are(
    leaf.parent, [None, token.NEWLINE, token.INDENT, syms.simple_stmt]
):
    _l_(5089)

    aux = True
    _l_(5088)
    exit(aux)

# Multiline docstring on the same line as the `def`.
if prev_siblings_are(leaf.parent, [syms.parameters, token.COLON, syms.simple_stmt]):
    _l_(5091)

    aux = True
    _l_(5090)
    # `syms.parameters` is only used in funcdefs and async_funcdefs in the Python
    # grammar. We're safe to return True without further checks.
    exit(aux)
aux = False
_l_(5092)

exit(aux)
