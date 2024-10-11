from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3 import pytree # pragma: no cover
from lib2to3.refactor import RefactoringTool # pragma: no cover
from typing import Any # pragma: no cover
from typing_extensions import Protocol # pragma: no cover

class DebugVisitor(Protocol): # pragma: no cover
    def visit(self, node: pytree.Node) -> Any: # pragma: no cover
        return [] # pragma: no cover
 # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
 # pragma: no cover
def lib2to3_parse(input_code: str) -> pytree.Node: # pragma: no cover
    drv = driver.Driver(driver.PyGrammar(), convert=pytree.convert) # pragma: no cover
    return drv.parse_string(input_code) # pragma: no cover

from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3 import pytree # pragma: no cover
from lib2to3.refactor import RefactoringTool # pragma: no cover
import ast # pragma: no cover

class DebugVisitor(ast.NodeVisitor): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover
 # pragma: no cover
    def visit(self, node: pytree.Node): # pragma: no cover
        super().visit(node) # pragma: no cover
        return [] # pragma: no cover
 # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
 # pragma: no cover
def lib2to3_parse(input_code: str) -> pytree.Node: # pragma: no cover
    drv = driver.Driver(driver.PyGrammar(), convert=pytree.convert) # pragma: no cover
    return drv.parse_string(input_code) # pragma: no cover

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
