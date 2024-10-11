from lib2to3 import fixer_base # pragma: no cover
from lib2to3 import pgen2 # pragma: no cover
from lib2to3.pgen2 import tokenize # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3 import refactor # pragma: no cover

class DebugVisitor(fixer_base.BaseFix): pass # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code): return driver.Driver().parse_string(code) # pragma: no cover

from lib2to3 import refactor # pragma: no cover
from lib2to3.pytree import Node # pragma: no cover
from lib2to3.pgen2 import parse # pragma: no cover

class DebugVisitor(refactor.RefactoringTool):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__([], None)  # options and log as arguments# pragma: no cover
    def visit(self, node):# pragma: no cover
        print(node)# pragma: no cover
        return node # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code):# pragma: no cover
    return parse(code, None) # pragma: no cover

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
