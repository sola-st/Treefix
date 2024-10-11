from typing import List, Any # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def __init__(self, depth: int): # pragma: no cover
        self.depth = depth # pragma: no cover
 # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, leaf_type: str): # pragma: no cover
        self.type = leaf_type # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, is_comment: bool, leaves: List[Any], depth: int): # pragma: no cover
        self.bracket_tracker = MockBracketTracker(depth) # pragma: no cover
        self.is_comment = is_comment # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
    def append(self, leaf: Any, preformatted: bool): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover
 # pragma: no cover
self = MockSelf(is_comment=True, leaves=[], depth=0) # pragma: no cover
leaf = MockLeaf(leaf_type=STANDALONE_COMMENT) # pragma: no cover
preformatted = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Like :func:`append()` but disallow invalid standalone comment structure.

        Raises ValueError when any `leaf` is appended after a standalone comment
        or when a standalone comment is not the first leaf on the line.
        """
if self.bracket_tracker.depth == 0:
    _l_(17520)

    if self.is_comment:
        _l_(17517)

        raise ValueError("cannot append to standalone comments")
        _l_(17516)

    if self.leaves and leaf.type == STANDALONE_COMMENT:
        _l_(17519)

        raise ValueError(
            "cannot append standalone comments to a populated line"
        )
        _l_(17518)

self.append(leaf, preformatted=preformatted)
_l_(17521)
