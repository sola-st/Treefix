import token # pragma: no cover
from collections import namedtuple # pragma: no cover

MockLeaf = namedtuple('MockLeaf', ['parent']) # pragma: no cover
leaf = MockLeaf(parent=None) # pragma: no cover
token.NEWLINE = 4 # pragma: no cover
token.INDENT = 5 # pragma: no cover
mock_syms = type('MockSyms', (object,), {'simple_stmt': 6, 'parameters': 7}) # pragma: no cover
syms = mock_syms() # pragma: no cover
def prev_siblings_are(parent, siblings): return True if parent is None else False # pragma: no cover

import token # pragma: no cover
from collections import namedtuple # pragma: no cover

MockLeaf = namedtuple('MockLeaf', ['parent']) # pragma: no cover
leaf = MockLeaf(parent=None) # pragma: no cover
token.NEWLINE = 4 # pragma: no cover
token.INDENT = 5 # pragma: no cover
token.COLON = 6 # pragma: no cover
mock_syms = type('MockSyms', (object,), {'simple_stmt': 7, 'parameters': 8}) # pragma: no cover
syms = mock_syms() # pragma: no cover
def prev_siblings_are(parent, siblings): return True if parent is None else False # pragma: no cover

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
