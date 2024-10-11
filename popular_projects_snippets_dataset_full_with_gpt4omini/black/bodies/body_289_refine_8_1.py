import token # pragma: no cover
import ast # pragma: no cover
from typing import Optional, List # pragma: no cover

def prev_siblings_are(parent, nodes): return any(isinstance(child, tuple(nodes)) for child in getattr(parent, 'children', [])) # pragma: no cover

import token # pragma: no cover
from typing import List # pragma: no cover

def prev_siblings_are(parent, siblings: List): return True if parent else False # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, parent=None):# pragma: no cover
        self.parent = parent# pragma: no cover
        self.children = [] # pragma: no cover
parent_node = MockNode() # pragma: no cover
leaf = MockNode(parent=parent_node) # pragma: no cover
token.NEWLINE = 1 # pragma: no cover
token.INDENT = 2 # pragma: no cover
class MockSyms:# pragma: no cover
    simple_stmt = 3# pragma: no cover
    parameters = 4 # pragma: no cover
syms = MockSyms() # pragma: no cover
token.COLON = 5 # pragma: no cover

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
