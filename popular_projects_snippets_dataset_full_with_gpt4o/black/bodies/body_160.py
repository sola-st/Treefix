# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Remove the trailing comma and moves the comments attached to it."""
trailing_comma = self.leaves.pop()
_l_(17238)
trailing_comma_comments = self.comments.pop(id(trailing_comma), [])
_l_(17239)
self.comments.setdefault(id(self.leaves[-1]), []).extend(
    trailing_comma_comments
)
_l_(17240)
