from typing import TypeVar, Generic # pragma: no cover
from lib2to3.pgen2.parse import ParseError # pragma: no cover
from lib2to3.pgen2.tokenize import TokenError # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover
from lib2to3.pgen2.driver import Driver # pragma: no cover
from lib2to3 import pytree # pragma: no cover

T = TypeVar('T') # pragma: no cover
class DebugVisitor(Generic[T]): # pragma: no cover
    def visit(self, node: pytree.Node) -> None: # pragma: no cover
        # Mock visit method, replace with actual implementation if needed # pragma: no cover
        yield # pragma: no cover
def lib2to3_parse(code: str) -> pytree.Node: # pragma: no cover
    driver = Driver(python_grammar, pytree.convert) # pragma: no cover
    try: # pragma: no cover
        return driver.parse_string(code, True) # pragma: no cover
    except (ParseError, TokenError) as e: # pragma: no cover
        return None # pragma: no cover
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
