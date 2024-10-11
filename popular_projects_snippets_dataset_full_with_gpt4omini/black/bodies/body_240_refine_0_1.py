from lib2to3 import fixer_base # pragma: no cover
from lib2to3 import pgen2 # pragma: no cover

code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code):# pragma: no cover
    return refactor.MakeTree(refactor.Refactorer(), code) # pragma: no cover

from lib2to3 import fixer_base # pragma: no cover
from lib2to3 import pgen2 # pragma: no cover

code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code):# pragma: no cover
    refactorer = Refactorer()# pragma: no cover
    return refactorer.parse_string(code) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/debug.py
from l3.Runtime import _l_
"""Pretty-print the lib2to3 AST of a given string of `code`.

        Convenience method for debugging.
        """
v: DebugVisitor[None] = DebugVisitor()
_l_(7671)
if isinstance(code, str):
    _l_(7673)

    code = lib2to3_parse(code)
    _l_(7672)
list(v.visit(code))
_l_(7674)
