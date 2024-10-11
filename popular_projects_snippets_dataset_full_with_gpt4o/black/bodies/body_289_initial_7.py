import token # pragma: no cover
from types import SimpleNamespace # pragma: no cover

prev_siblings_are = lambda parent, types: True # pragma: no cover
leaf = SimpleNamespace(parent=None) # pragma: no cover
syms = type('Mock', (object,), {'simple_stmt': 'fake_simple_stmt', 'parameters': 'fake_parameters'}) # pragma: no cover
token.NEWLINE = 'fake_newline' # pragma: no cover
token.INDENT = 'fake_indent' # pragma: no cover
token.COLON = 'fake_colon' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
if prev_siblings_are(
    leaf.parent, [None, token.NEWLINE, token.INDENT, syms.simple_stmt]
):
    _l_(16749)

    aux = True
    _l_(16748)
    exit(aux)

# Multiline docstring on the same line as the `def`.
if prev_siblings_are(leaf.parent, [syms.parameters, token.COLON, syms.simple_stmt]):
    _l_(16751)

    aux = True
    _l_(16750)
    # `syms.parameters` is only used in funcdefs and async_funcdefs in the Python
    # grammar. We're safe to return True without further checks.
    exit(aux)
aux = False
_l_(16752)

exit(aux)
