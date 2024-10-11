from typing import List # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def __init__(self, depth: int): # pragma: no cover
        self.depth = depth # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type_: str): # pragma: no cover
        self.type = type_ # pragma: no cover
 # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, leaves: List[Leaf], is_comment: bool, depth: int): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.is_comment = is_comment # pragma: no cover
        self.bracket_tracker = MockBracketTracker(depth) # pragma: no cover
    def append(self, leaf: Leaf, preformatted: bool): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
# To trigger 'raise ValueError("cannot append to standalone comments")' # pragma: no cover
self = MockSelf(leaves=[], is_comment=True, depth=0) # pragma: no cover
leaf = Leaf(type_='any_type') # pragma: no cover
preformatted = False # pragma: no cover
 # pragma: no cover
# Uncomment the following lines to instead trigger 'raise ValueError("cannot append standalone comments to a populated line")' # pragma: no cover
# self = MockSelf(leaves=[Leaf(type_='token')], is_comment=False, depth=0) # pragma: no cover
# leaf = Leaf(type_=STANDALONE_COMMENT) # pragma: no cover

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
