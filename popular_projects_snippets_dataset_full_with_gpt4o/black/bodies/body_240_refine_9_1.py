from lib2to3.pytree import Node, Leaf # pragma: no cover
from lib2to3.pgen2.token import NAME, NEWLINE # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover
from lib2to3 import refactor # pragma: no cover
from typing import Any # pragma: no cover

class DebugVisitor:# pragma: no cover
    def __init__(self) -> None:# pragma: no cover
        self.depth = 0# pragma: no cover
        # pragma: no cover
    def visit(self, node: Any) -> None:# pragma: no cover
        self.depth += 1# pragma: no cover
        indent = ' ' * (self.depth * 2)# pragma: no cover
        print(f'{indent}{node}')# pragma: no cover
        if hasattr(node, 'children'):# pragma: no cover
            for child in node.children:# pragma: no cover
                self.visit(child)# pragma: no cover
        self.depth -= 1 # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover
def lib2to3_parse(code: str) -> Node:# pragma: no cover
    grammar = python_grammar.copy()# pragma: no cover
    driver = refactor.Driver(grammar, convert=pytree.convert)# pragma: no cover
    return driver.parse_string(code, True) # pragma: no cover

from lib2to3.pytree import Node, Leaf # pragma: no cover
from lib2to3.pgen2.driver import Driver # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover
from typing import Any # pragma: no cover

class DebugVisitor:# pragma: no cover
    def visit(self, node: Any) -> None:# pragma: no cover
        if isinstance(node, Node):# pragma: no cover
            for child in node.children:# pragma: no cover
                self.visit(child)# pragma: no cover
        elif isinstance(node, Leaf):# pragma: no cover
            print(node.value) # pragma: no cover
code = 'print("Hello, World!")' # pragma: no cover

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
