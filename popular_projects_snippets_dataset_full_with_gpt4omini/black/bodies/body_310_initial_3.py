import token # pragma: no cover

class MockLeaf: pass # pragma: no cover
leaf = MockLeaf() # pragma: no cover
leaf.type = token.LPAR # pragma: no cover
leaf.value = '' # pragma: no cover
token.LPAR = 'LPAR' # pragma: no cover
token.RPAR = 'RPAR' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Make sure parentheses are visible.

    They could be invisible as part of some statements (see
    :func:`normalize_invisible_parens` and :func:`visit_import_from`).
    """
if leaf.type == token.LPAR:
    _l_(6597)

    leaf.value = "("
    _l_(6594)
elif leaf.type == token.RPAR:
    _l_(6596)

    leaf.value = ")"
    _l_(6595)
