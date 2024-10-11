def is_empty_lpar(leaf): return not leaf.get('left', None) # pragma: no cover
leaf = {'left': None, 'right': None} # pragma: no cover
def is_empty_rpar(leaf): return not leaf.get('right', None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = is_empty_lpar(leaf) or is_empty_rpar(leaf)
_l_(5788)
exit(aux)
