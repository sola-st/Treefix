from typing import Any # pragma: no cover

token = type('MockToken', (object,), {'LPAR': 1, 'RPAR': 2})() # pragma: no cover
leaf = type('MockLeaf', (object,), {'type': None, 'value': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Make sure parentheses are visible.

    They could be invisible as part of some statements (see
    :func:`normalize_invisible_parens` and :func:`visit_import_from`).
    """
if leaf.type == token.LPAR:
    _l_(18369)

    leaf.value = "("
    _l_(18366)
elif leaf.type == token.RPAR:
    _l_(18368)

    leaf.value = ")"
    _l_(18367)
