import types # pragma: no cover

self = type('Mock', (object,), {'comments': {}})() # pragma: no cover
leaf = object() # pragma: no cover
self.comments[id(leaf)] = ['This is a comment', 'Another comment'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Generate comments that should appear directly after `leaf`."""
aux = self.comments.get(id(leaf), [])
_l_(19751)
exit(aux)
