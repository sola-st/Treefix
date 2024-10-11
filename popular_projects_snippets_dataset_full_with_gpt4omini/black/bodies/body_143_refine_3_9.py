from typing import List # pragma: no cover

preformatted = False # pragma: no cover

class BracketTracker: depth = 0 # pragma: no cover
class Leaf: type = 'standalone_comment' # pragma: no cover
class Mock:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = BracketTracker() # pragma: no cover
        self.is_comment = False # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.append = lambda leaf, preformatted: self.leaves.append(leaf) # pragma: no cover
self = Mock() # pragma: no cover
leaf = Leaf() # pragma: no cover
preformatted = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Like :func:`append()` but disallow invalid standalone comment structure.

        Raises ValueError when any `leaf` is appended after a standalone comment
        or when a standalone comment is not the first leaf on the line.
        """
if self.bracket_tracker.depth == 0:
    _l_(5666)

    if self.is_comment:
        _l_(5663)

        raise ValueError("cannot append to standalone comments")
        _l_(5662)

    if self.leaves and leaf.type == STANDALONE_COMMENT:
        _l_(5665)

        raise ValueError(
            "cannot append standalone comments to a populated line"
        )
        _l_(5664)

self.append(leaf, preformatted=preformatted)
_l_(5667)
