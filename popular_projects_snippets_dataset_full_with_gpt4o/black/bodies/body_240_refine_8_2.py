from lib2to3.pytree import Node # pragma: no cover
from lib2to3.pygram import python_grammar as grammar # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover

DebugVisitor = type('DebugVisitor', (object,), {'visit': lambda self, node: [node]}) # pragma: no cover
lib2to3_parse = lambda code: RefactoringTool(get_fixers_from_package('lib2to3.fixes')).refactor_string(code, '<string>') # pragma: no cover

from lib2to3.pytree import Node # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover
from lib2to3.refactor import RefactoringTool, get_fixers_from_package # pragma: no cover

class DebugVisitor:# pragma: no cover
    def visit(self, node: Node):# pragma: no cover
        nodes = [node]# pragma: no cover
        while nodes:# pragma: no cover
            current_node = nodes.pop(0)# pragma: no cover
            print(f'Visiting: {current_node}')# pragma: no cover
            if isinstance(current_node, Node):# pragma: no cover
                nodes.extend(current_node.children)# pragma: no cover
        return node # pragma: no cover
def lib2to3_parse(code: str) -> Node:# pragma: no cover
    rt = RefactoringTool(get_fixers_from_package('lib2to3.fixes'))# pragma: no cover
    return rt.refactor_string(code, '<string>') # pragma: no cover

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
