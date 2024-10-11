from typing import List # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.depth = 0 # pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, leaf_type):# pragma: no cover
        self.type = leaf_type # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
preformatted = True # pragma: no cover
self = type('Mock', (object,), {'bracket_tracker': MockBracketTracker(), 'is_comment': False, 'leaves': []})() # pragma: no cover
leaf = MockLeaf(STANDALONE_COMMENT) # pragma: no cover

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
