from collections import namedtuple # pragma: no cover

class Mock: pass # pragma: no cover
Mock.bracket_tracker = type('BracketTracker', (), {'depth': 0})() # pragma: no cover
Mock.is_comment = False # pragma: no cover
Mock.leaves = [] # pragma: no cover
leaf = namedtuple('Leaf', ['type'])(type='STANDALONE_COMMENT') # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover
def append(leaf, preformatted): return None # pragma: no cover
Mock.append = append # pragma: no cover

from typing import List # pragma: no cover

class MockBracketTracker: depth = 0 # pragma: no cover
class MockLeaf: type = 'STANDALONE_COMMENT' # pragma: no cover

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
