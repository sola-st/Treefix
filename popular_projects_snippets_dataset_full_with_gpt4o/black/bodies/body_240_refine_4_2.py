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

from lib2to3.pgen2.parse import ParseError # pragma: no cover
from lib2to3.pytree import Node, Leaf # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover
from typing import Any # pragma: no cover

class DebugVisitor:# pragma: no cover
    def __init__(self) -> None:# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
    def visit(self, node: Any) -> None:# pragma: no cover
        print(f'Visiting node: {node}') # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
def lib2to3_parse(code: str) -> Node:# pragma: no cover
    rt = RefactoringTool(get_fixers_from_package("lib2to3.fixes"))# pragma: no cover
    try:# pragma: no cover
        return rt.refactor_string(code, 'example')# pragma: no cover
    except ParseError as pe:# pragma: no cover
        raise pe # pragma: no cover

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
