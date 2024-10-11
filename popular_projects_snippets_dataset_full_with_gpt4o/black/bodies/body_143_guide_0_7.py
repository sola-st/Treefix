from typing import Any, List # pragma: no cover

class Leaf: pass # pragma: no cover
 # pragma: no cover
class BracketTracker: # pragma: no cover
    depth: int = 0 # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    leaves: List[Leaf] = [] # pragma: no cover
    is_comment: bool = False # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = BracketTracker() # pragma: no cover
    def append(self, leaf: Any, preformatted: bool = False) -> None: # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
leaf = Leaf() # pragma: no cover
leaf.type = STANDALONE_COMMENT # pragma: no cover
preformatted = False # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
self.leaves.append(Leaf()) # pragma: no cover

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
