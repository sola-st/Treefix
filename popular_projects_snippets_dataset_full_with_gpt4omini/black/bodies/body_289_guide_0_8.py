import token # pragma: no cover
import typing # pragma: no cover
from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['parent']) # pragma: no cover
syms = type('Mock', (object,), {'simple_stmt': 1, 'parameters': 2})() # pragma: no cover
leaf = Leaf(parent=type('Mock', (object,), {'children': []})()) # pragma: no cover
def prev_siblings_are(parent, siblings): return any(sibling in parent.children for sibling in siblings) # pragma: no cover

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
