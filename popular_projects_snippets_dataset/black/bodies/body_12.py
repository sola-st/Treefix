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
