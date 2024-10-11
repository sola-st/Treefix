import token # pragma: no cover
class Leaf: pass # pragma: no cover
class Mock: pass # pragma: no cover

leaf = Leaf() # pragma: no cover
leaf.type = token.COMMENT # pragma: no cover
leaf.value = '# type: ignore' # pragma: no cover
STANDALONE_COMMENT = 2 # pragma: no cover
suffix = 'ignore' # pragma: no cover
token.COMMENT = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if the given leaf is a special comment.
    Only returns true for type comments for now."""
t = leaf.type
_l_(7025)
v = leaf.value
_l_(7026)
aux = t in {token.COMMENT, STANDALONE_COMMENT} and v.startswith("# type:" + suffix)
_l_(7027)
exit(aux)
