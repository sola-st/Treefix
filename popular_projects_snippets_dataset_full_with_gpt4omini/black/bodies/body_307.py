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
