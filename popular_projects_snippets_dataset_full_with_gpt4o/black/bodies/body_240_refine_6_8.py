from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3 import pygram # pragma: no cover
from lib2to3.pytree import Node, Leaf # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover
import lib2to3.pytree # pragma: no cover
from typing import Generic, TypeVar # pragma: no cover

T = TypeVar('T') # pragma: no cover
class DebugVisitor(Generic[T]): # pragma: no cover
    def visit(self, node: 'lib2to3.pytree.Node') -> None: # pragma: no cover
        for child in node.children: # pragma: no cover
            print(child) # pragma: no cover
            if isinstance(child, lib2to3.pytree.Node): # pragma: no cover
                self.visit(child) # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
lib2to3_parse = driver.Driver(python_grammar, convert=lib2to3.pytree.convert).parse_string # pragma: no cover

from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover
from lib2to3.pgen2.parse import ParseError # pragma: no cover
from lib2to3 import pytree # pragma: no cover

class DebugVisitor: # pragma: no cover
    def visit(self, node): # pragma: no cover
        print(f'Visiting node: {node}') # pragma: no cover
        for child in node.children: # pragma: no cover
            self.visit(child) # pragma: no cover
code = 'print("Hello, world!")' # pragma: no cover
def lib2to3_parse(source: str): # pragma: no cover
    rt = RefactoringTool(get_fixers_from_package('lib2to3.fixes')) # pragma: no cover
    try: # pragma: no cover
        return rt.refactor_string(source, '<stdin>') # pragma: no cover
    except ParseError as e: # pragma: no cover
        print(f'ParseError: {e}') # pragma: no cover

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
