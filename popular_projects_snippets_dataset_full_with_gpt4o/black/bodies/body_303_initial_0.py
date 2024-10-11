def is_empty_lpar(leaf):# pragma: no cover
    return leaf == '(' # pragma: no cover
def is_empty_rpar(leaf):# pragma: no cover
    return leaf == ')' # pragma: no cover
leaf = '(' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = is_empty_lpar(leaf) or is_empty_rpar(leaf)
_l_(17209)
exit(aux)
