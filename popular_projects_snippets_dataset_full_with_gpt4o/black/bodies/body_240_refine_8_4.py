from lib2to3.pytree import Node # pragma: no cover
from lib2to3.pygram import python_grammar as grammar # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover

DebugVisitor = type('DebugVisitor', (object,), {'visit': lambda self, node: [node]}) # pragma: no cover
lib2to3_parse = lambda code: RefactoringTool(get_fixers_from_package('lib2to3.fixes')).refactor_string(code, '<string>') # pragma: no cover

from lib2to3.pytree import Node # pragma: no cover
from lib2to3.pygram import python_grammar as grammar # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover

class DebugVisitor:# pragma: no cover
    def visit(self, node: Node) -> None:# pragma: no cover
        for child in node.children:# pragma: no cover
            print(child)# pragma: no cover
            if isinstance(child, Node):# pragma: no cover
                self.visit(child) # pragma: no cover
lib2to3_parse = lambda code: RefactoringTool(get_fixers_from_package('lib2to3.fixes')).refactor_string(code, '<string>') # pragma: no cover

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
