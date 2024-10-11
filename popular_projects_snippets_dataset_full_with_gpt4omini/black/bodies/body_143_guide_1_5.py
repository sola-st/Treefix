class MockLeaf: # pragma: no cover
    def __init__(self, leaf_type): # pragma: no cover
        self.type = leaf_type # pragma: no cover
 # pragma: no cover
class MockBracketTracker: # pragma: no cover
    def __init__(self, depth): # pragma: no cover
        self.depth = depth # pragma: no cover
 # pragma: no cover
class MockObject: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = MockBracketTracker(0) # pragma: no cover
        self.is_comment = True # pragma: no cover
# Set to True to cover the first uncovered line # pragma: no cover
        self.leaves = [] # pragma: no cover
    def append(self, leaf, preformatted=None): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
# Simple append method # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover

self = MockObject() # pragma: no cover
leaf = MockLeaf(STANDALONE_COMMENT) # pragma: no cover
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
