from unittest.mock import Mock # pragma: no cover

prev_siblings_are = Mock(return_value=False) # pragma: no cover
leaf = Mock() # pragma: no cover
leaf.parent = Mock() # pragma: no cover
token = Mock() # pragma: no cover
token.NEWLINE = Mock() # pragma: no cover
token.INDENT = Mock() # pragma: no cover
token.COLON = Mock() # pragma: no cover
syms = Mock() # pragma: no cover
syms.simple_stmt = Mock() # pragma: no cover
syms.parameters = Mock() # pragma: no cover

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
