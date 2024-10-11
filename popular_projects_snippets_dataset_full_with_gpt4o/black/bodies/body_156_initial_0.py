is_multiline_string = lambda x: isinstance(x, str) and '\n' in x # pragma: no cover
self = type('Mock', (object,), {'leaves': ['leaf1', 'leaf2', 'leaf3\nleaf4']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
aux = any(is_multiline_string(leaf) for leaf in self.leaves)
_l_(16051)
exit(aux)
