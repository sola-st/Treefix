from collections import defaultdict # pragma: no cover

self = type('Mock', (), {})() # pragma: no cover
self.leaves = ['item1', 'item2', 'item3', ','] # pragma: no cover
self.comments = defaultdict(list) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Remove the trailing comma and moves the comments attached to it."""
trailing_comma = self.leaves.pop()
_l_(5524)
trailing_comma_comments = self.comments.pop(id(trailing_comma), [])
_l_(5525)
self.comments.setdefault(id(self.leaves[-1]), []).extend(
    trailing_comma_comments
)
_l_(5526)
