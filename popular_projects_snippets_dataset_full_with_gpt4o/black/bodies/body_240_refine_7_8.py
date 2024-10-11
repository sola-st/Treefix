from lib2to3 import refactor # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3.pygram import python_grammar_no_print_statement as grammar # pragma: no cover
from typing import Any # pragma: no cover
class DebugVisitor(refactor.RefactoringTool): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super().__init__(grammar, {}, *args, **kwargs) # pragma: no cover
    def visit(self, node: Any) -> list: # pragma: no cover
        return [] # pragma: no cover

code = 'def example_function():\n    pass' # pragma: no cover

from lib2to3.pgen2 import driver, parse, token # pragma: no cover
from lib2to3 import pytree, pygram # pragma: no cover
from typing import Any # pragma: no cover

class DebugVisitor: # pragma: no cover
    def visit(self, node: pytree.Node) -> Any: # pragma: no cover
        for child in node.children: # pragma: no cover
            print(child) # pragma: no cover
            if isinstance(child, pytree.Node): # pragma: no cover
                self.visit(child) # pragma: no cover
 # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
 # pragma: no cover
def lib2to3_parse(source: str) -> pytree.Node: # pragma: no cover
    grammar = pygram.python_grammar_no_print_statement # pragma: no cover
    drv = driver.Driver(grammar, pytree.convert) # pragma: no cover
    return drv.parse_string(source) # pragma: no cover

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
