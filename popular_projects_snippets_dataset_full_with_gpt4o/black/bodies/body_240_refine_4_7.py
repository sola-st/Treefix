from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3 import pytree # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover
from lib2to3.pygram import python_grammar_no_print_statement # pragma: no cover
from lib2to3 import fixer_util # pragma: no cover
from lib2to3.pytree import Node, Leaf # pragma: no cover
from lib2to3.refactor import RefactoringTool # pragma: no cover

code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(source: str):# pragma: no cover
    g = python_grammar_no_print_statement# pragma: no cover
    p = driver.Driver(g, pytree.convert)# pragma: no cover
    return p.parse_string(source, True) # pragma: no cover

from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3 import pytree # pragma: no cover
from lib2to3.pygram import python_grammar_no_print_statement # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover

class DebugVisitor:# pragma: no cover
    def visit(self, node):# pragma: no cover
        print(f'Visiting node: {node}') # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code: str) -> pytree.Node:# pragma: no cover
    drv = driver.Driver(python_grammar_no_print_statement, pytree.convert)# pragma: no cover
    return drv.parse_string(code) # pragma: no cover

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
