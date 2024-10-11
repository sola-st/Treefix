from enum import Enum # pragma: no cover
from typing import List, Any # pragma: no cover

class LeafType(Enum): # pragma: no cover
    STANDALONE_COMMENT = 1 # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type: LeafType): # pragma: no cover
        self.type = type # pragma: no cover
 # pragma: no cover
class BracketTracker: # pragma: no cover
    def __init__(self, depth: int): # pragma: no cover
        self.depth = depth # pragma: no cover
 # pragma: no cover
class SelfMock: # pragma: no cover
    def __init__(self, depth: int, is_comment: bool, leaves: List[Leaf]): # pragma: no cover
        self.bracket_tracker = BracketTracker(depth) # pragma: no cover
        self.is_comment = is_comment # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.append = lambda leaf, preformatted: None # pragma: no cover
 # pragma: no cover
# Creating an instance of SelfMock to test uncovered path where is_comment is True # pragma: no cover
self = SelfMock(depth=0, is_comment=True, leaves=[]) # pragma: no cover
 # pragma: no cover
# Placeholder leaf argument with any necessary type # pragma: no cover
leaf = Leaf(LeafType.STANDALONE_COMMENT) # pragma: no cover
preformatted = True # pragma: no cover

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
