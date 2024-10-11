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

from lib2to3.pgen2.driver import Driver # pragma: no cover
from lib2to3.pgen2.parse import ParseError # pragma: no cover
from lib2to3.pytree import Node, Leaf, convert # pragma: no cover
from lib2to3.pygram import python_grammar_no_print_statement as python_grammar # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover
from typing import Any # pragma: no cover

class DebugVisitor:# pragma: no cover
    def __init__(self) -> None:# pragma: no cover
        pass# pragma: no cover
    def visit(self, node: Any) -> None:# pragma: no cover
        if isinstance(node, Node) or isinstance(node, Leaf):# pragma: no cover
            print(f'Visiting node: {node}')# pragma: no cover
        return node # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(source: str) -> Node:# pragma: no cover
    driver = Driver(python_grammar, convert)# pragma: no cover
    try:# pragma: no cover
        return driver.parse_string(source)# pragma: no cover
    except ParseError as e:# pragma: no cover
        print(f'Error parsing code: {e}')# pragma: no cover
        raise # pragma: no cover

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
