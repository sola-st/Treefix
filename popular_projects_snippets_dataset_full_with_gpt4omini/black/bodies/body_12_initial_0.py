from typing import List, Callable # pragma: no cover
import keywords # pragma: no cover

def normalize_invisible_parens(node, parens_after, mode, features): pass # pragma: no cover
node = type('MockNode', (object,), {'children': []})() # pragma: no cover
parens = ['function', 'class', 'if'] # pragma: no cover
self = type('MockSelf', (object,), {'mode': 'default_mode', 'features': []})() # pragma: no cover
def is_name_token(child): return isinstance(child, str) and len(child) > 0 # pragma: no cover
keywords = ['if', 'else', 'while', 'for', 'def', 'class'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Visit a statement.

        This implementation is shared for `if`, `while`, `for`, `try`, `except`,
        `def`, `with`, `class`, `assert`, and assignments.

        The relevant Python language `keywords` for a given statement will be
        NAME leaves within it. This methods puts those on a separate line.

        `parens` holds a set of string leaf values immediately after which
        invisible parens should be put.
        """
normalize_invisible_parens(
    node, parens_after=parens, mode=self.mode, features=self.features
)
_l_(7334)
for child in node.children:
    _l_(7338)

    if is_name_token(child) and child.value in keywords:
        _l_(7336)

        aux = self.line()
        _l_(7335)
        exit(aux)
    aux = self.visit(child)
    _l_(7337)

    exit(aux)
