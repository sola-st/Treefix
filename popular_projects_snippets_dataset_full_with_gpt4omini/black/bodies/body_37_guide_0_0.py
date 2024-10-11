from typing import Collection, Iterator # pragma: no cover
from functools import wraps # pragma: no cover

class MockLeaf:  # defining a mock for Leaf object# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
 # pragma: no cover
class MockLine:  # defining a mock for Line object# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf, inside_brackets):  # mock function to simulate prefix normalization# pragma: no cover
    leaf.value = f'normalized_{leaf.value}'# pragma: no cover
 # pragma: no cover
def split_func(line: MockLine, features: Collection = ()):  # mock split function# pragma: no cover
    # simulating splitting the line into two leaves# pragma: no cover
    return [MockLine([MockLeaf('leaf1'), MockLeaf('leaf2')])]  # pragma: no cover
 # pragma: no cover
split_func = split_func  # to ensure it's the same as the one used in the decorator# pragma: no cover
 # pragma: no cover
line = MockLine([MockLeaf('original_leaf')])  # creating a mock Line instance# pragma: no cover
 # pragma: no cover
features = []  # initializing features as an empty list# pragma: no cover
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
