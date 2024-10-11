from typing import List # pragma: no cover

preformatted = False # pragma: no cover

class MockBracketTracker: depth = 0 # pragma: no cover
class MockLeaf: type = 'standalone_comment' # pragma: no cover
self = type('Mock', (object,), {'bracket_tracker': MockBracketTracker(), 'is_comment': False, 'leaves': [], 'append': lambda self, leaf, preformatted: self.leaves.append(leaf)})() # pragma: no cover
leaf = MockLeaf() # pragma: no cover
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
