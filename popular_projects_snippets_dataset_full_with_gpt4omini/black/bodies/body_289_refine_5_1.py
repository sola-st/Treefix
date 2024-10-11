import token # pragma: no cover
from collections import namedtuple # pragma: no cover

MockLeaf = namedtuple('MockLeaf', ['parent'])# pragma: no cover
leaf = MockLeaf(parent=None) # pragma: no cover
class MockToken:# pragma: no cover
    NEWLINE = 1# pragma: no cover
    INDENT = 2# pragma: no cover
    COLON = 3# pragma: no cover
# pragma: no cover
    # Simulating how token would generally be organized# pragma: no cover
token = MockToken() # pragma: no cover
class MockSyms:# pragma: no cover
    simple_stmt = 1# pragma: no cover
    parameters = 2# pragma: no cover
# pragma: no cover
syms = MockSyms() # pragma: no cover
def prev_siblings_are(parent, tokens):# pragma: no cover
    return True  # Simulating behavior for testing # pragma: no cover

import token # pragma: no cover
from collections import namedtuple # pragma: no cover

class MockParent:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.children = []# pragma: no cover
parent_node = MockParent() # pragma: no cover
MockLeaf = namedtuple('MockLeaf', ['parent'])# pragma: no cover
leaf = MockLeaf(parent=parent_node) # pragma: no cover
class MockToken:# pragma: no cover
    NEWLINE = 'newline'# pragma: no cover
    INDENT = 'indent'# pragma: no cover
    COLON = 'colon'# pragma: no cover
# pragma: no cover
    # Simulating how token would generally be organized# pragma: no cover
token = MockToken() # pragma: no cover
class MockSyms:# pragma: no cover
    simple_stmt = 'simple_stmt'# pragma: no cover
    parameters = 'parameters'# pragma: no cover
# pragma: no cover
syms = MockSyms() # pragma: no cover
def prev_siblings_are(parent, siblings):# pragma: no cover
    return True if parent and parent.children else False # pragma: no cover

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
