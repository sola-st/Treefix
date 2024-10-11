from lib2to3 import fixer_base # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover
from lib2to3 import pytree # pragma: no cover
from typing import Optional, Any, List # pragma: no cover

class DebugVisitor(fixer_base.BaseFix):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__()# pragma: no cover
    def visit(self, node: pytree.Node) -> List[Any]:# pragma: no cover
        return [str(node)] # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
def lib2to3_parse(code: str) -> pytree.Node:# pragma: no cover
    driver_instance = driver.Driver(fixer_base.FixerCollection(), (token.END,))# pragma: no cover
    return driver_instance.parse_string(code) # pragma: no cover

from lib2to3 import fixer_base # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover
from lib2to3 import pytree # pragma: no cover
from lib2to3 import refactor # pragma: no cover

class DebugVisitor(fixer_base.BaseFix):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__([], None, None)# pragma: no cover
    def visit(self, node: pytree.Node) -> str:# pragma: no cover
        return str(node) # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code: str) -> pytree.Node:# pragma: no cover
    tool = refactor.RefactoringTool([])# pragma: no cover
    return tool.refactor_string(code, 'dummy_filename') # pragma: no cover

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
