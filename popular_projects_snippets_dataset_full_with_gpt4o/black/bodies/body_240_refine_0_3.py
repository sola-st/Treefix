from lib2to3.pgen2.parse import ParseError # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover
import lib2to3.pytree # pragma: no cover
import ast # pragma: no cover

class DebugVisitor(ast.NodeVisitor):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        super().__init__(*args, **kwargs)# pragma: no cover
# pragma: no cover
    def visit(self, node):# pragma: no cover
        super().visit(node)# pragma: no cover
        return [] # pragma: no cover
code = 'print("Hello World")' # pragma: no cover
def lib2to3_parse(code):# pragma: no cover
    rt = RefactoringTool(get_fixers_from_package("lib2to3.fixes"))# pragma: no cover
    return rt.refactor_string(code, '<input>') # pragma: no cover

from lib2to3.pgen2.parse import ParseError # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover
import lib2to3.pytree # pragma: no cover
import ast # pragma: no cover

class DebugVisitor(ast.NodeVisitor):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        super().__init__(*args, **kwargs)# pragma: no cover
# pragma: no cover
    def visit(self, node):# pragma: no cover
        super().visit(node)# pragma: no cover
        return [] # pragma: no cover
v = DebugVisitor() # pragma: no cover
code = 'print("Hello World")' # pragma: no cover
def lib2to3_parse(code):# pragma: no cover
    rt = RefactoringTool(get_fixers_from_package("lib2to3.fixes"))# pragma: no cover
    return rt.refactor_string(code, '<input>') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/debug.py
from l3.Runtime import _l_
"""Pretty-print the lib2to3 AST of a given string of `code`.

        Convenience method for debugging.
        """
v: DebugVisitor[None] = DebugVisitor()
_l_(19562)
if isinstance(code, str):
    _l_(19564)

    code = lib2to3_parse(code)
    _l_(19563)
list(v.visit(code))
_l_(19565)
