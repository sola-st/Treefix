from typing import Collection, Iterator # pragma: no cover
from functools import wraps # pragma: no cover

class MockLeaf:  # A mock class to represent a leaf# pragma: no cover
    def __init__(self, text):# pragma: no cover
        self.text = text# pragma: no cover
 # pragma: no cover
class MockLine:  # A mock class to represent a line# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
 # pragma: no cover
def split_func(line: MockLine, features: Collection = ()) -> Iterator[MockLine]:  # A mock split function# pragma: no cover
    # This mock just returns the line passed to it# pragma: no cover
    yield line# pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf: MockLeaf, inside_brackets: bool):  # A mock normalize function# pragma: no cover
    leaf.text = f'Normalized: {leaf.text}'# pragma: no cover
 # pragma: no cover
line = MockLine([MockLeaf('example')])  # Initialize a MockLine with one MockLeaf# pragma: no cover
 # pragma: no cover
features = []  # Sample features, empty for this example# pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Normalize prefix of the first leaf in every line returned by `split_func`.

    This is a decorator over relevant split functions.
    """

@wraps(split_func)
def split_wrapper(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]:
    _l_(7176)

    for split_line in split_func(line, features):
        _l_(7175)

        normalize_prefix(split_line.leaves[0], inside_brackets=True)
        _l_(7173)
        aux = split_line
        _l_(7174)
        exit(aux)
aux = split_wrapper
_l_(7177)

exit(aux)
