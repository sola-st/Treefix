from lib2to3.pgen2.driver import Driver # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover
from lib2to3.pytree import Node # pragma: no cover
from lib2to3 import pytree # pragma: no cover

class DebugVisitor: # pragma: no cover
    def visit(self, node): # pragma: no cover
        # Mock implementation for the visit function # pragma: no cover
        if isinstance(node, Node): # pragma: no cover
            for child in node.children: # pragma: no cover
                self.visit(child) # pragma: no cover
        return [node] # pragma: no cover
 # pragma: no cover
def lib2to3_parse(code): # pragma: no cover
    driver = Driver(python_grammar, pytree.convert) # pragma: no cover
    return driver.parse_string(code) # pragma: no cover
 # pragma: no cover
code = "print('Hello, World!')" # pragma: no cover

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
