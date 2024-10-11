from typing import List, Any # pragma: no cover

class Mock: pass # pragma: no cover
def prev_siblings_are(node: Any, siblings: List[Any]) -> bool: return True # pragma: no cover
leaf = Mock() # pragma: no cover
leaf.parent = Mock() # pragma: no cover
token = Mock() # pragma: no cover
token.NEWLINE = 'NEWLINE' # pragma: no cover
token.INDENT = 'INDENT' # pragma: no cover
syms = Mock() # pragma: no cover
syms.simple_stmt = 'simple_stmt' # pragma: no cover
syms.parameters = 'parameters' # pragma: no cover
token.COLON = 'COLON' # pragma: no cover

from typing import List, Any # pragma: no cover

class Mock: pass # pragma: no cover
def prev_siblings_are(node: Any, siblings: List[Any]) -> bool: return isinstance(node, Mock) and all(isinstance(s, str) for s in siblings) # pragma: no cover
leaf = Mock() # pragma: no cover
leaf.parent = Mock() # pragma: no cover
token = type('Mock', (object,), {'NEWLINE': 'NEWLINE', 'INDENT': 'INDENT', 'COLON': 'COLON'}) # pragma: no cover
syms = type('Mock', (object,), {'simple_stmt': 'simple_stmt', 'parameters': 'parameters'}) # pragma: no cover

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
