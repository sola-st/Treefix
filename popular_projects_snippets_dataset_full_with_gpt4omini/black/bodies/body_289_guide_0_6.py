import token # pragma: no cover
import lib2to3.pgen2.token as token # pragma: no cover
from lib2to3 import pygram # pragma: no cover
from lib2to3.pgen2 import driver, parse # pragma: no cover
from lib2to3 import fixer_base, refactor # pragma: no cover

class MockLeaf: pass # pragma: no cover
leaf = MockLeaf() # pragma: no cover
leaf.parent = MockLeaf() # pragma: no cover
leaf.parent.children = [] # pragma: no cover
def prev_siblings_are(parent, tokens): return True # pragma: no cover
token.NEWLINE = 'NEWLINE' # pragma: no cover
token.INDENT = 'INDENT' # pragma: no cover
token.COLON = 'COLON' # pragma: no cover
aux = None # pragma: no cover

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
