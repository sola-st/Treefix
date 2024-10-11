import token # pragma: no cover
from typing import Any, List # pragma: no cover

def prev_siblings_are(parent: Any, siblings: List[Any]) -> bool: return True # pragma: no cover
class MockLeaf: parent = None # pragma: no cover
leaf = MockLeaf() # pragma: no cover
class MockToken: NEWLINE = 'NEWLINE'; INDENT = 'INDENT'; COLON = 'COLON' # pragma: no cover
token = MockToken() # pragma: no cover
class MockSyms: simple_stmt = 'simple_stmt'; parameters = 'parameters' # pragma: no cover
syms = MockSyms() # pragma: no cover

import token # pragma: no cover
from typing import List, Any # pragma: no cover

def prev_siblings_are(parent: Any, siblings: List[Any]) -> bool: return True # pragma: no cover

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
