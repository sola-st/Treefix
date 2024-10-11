from typing import Set, Any, List # pragma: no cover

def normalize_invisible_parens(node: Any, parens_after: Set[str], mode: Any, features: Any): pass # pragma: no cover
node = type('Node', (object,), {'children': []})() # pragma: no cover
parens = set() # pragma: no cover
self = type('Mock', (object,), {'mode': None, 'features': None, 'line': lambda: None, 'visit': lambda child: None})() # pragma: no cover
def is_name_token(child: Any) -> bool: return hasattr(child, 'value') # pragma: no cover
keywords = set() # pragma: no cover

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
_l_(18897)
for child in node.children:
    _l_(18901)

    if is_name_token(child) and child.value in keywords:
        _l_(18899)

        aux = self.line()
        _l_(18898)
        exit(aux)
    aux = self.visit(child)
    _l_(18900)

    exit(aux)
