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
def split_func(line: MockLine, features: Collection = ()) -> Iterator[MockLine]:  # Mock split function that yields a line# pragma: no cover
    yield MockLine([MockLeaf('leaf1')])  # Yielding one mock line with a leaf# pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf: MockLeaf, inside_brackets: bool):  # Mock normalization function# pragma: no cover
    leaf.text = f'normalized_{leaf.text}' # pragma: no cover
line = MockLine([MockLeaf('initial_leaf')])  # Create a mock line with one leaf# pragma: no cover
 # pragma: no cover
features = []  # Initialize features as an empty list # pragma: no cover
split_wrapper = wraps(split_func)(lambda line, features: split_func(line, features))  # Define split_wrapper function # pragma: no cover

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
