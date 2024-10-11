from typing import Collection, Iterator # pragma: no cover
from functools import wraps # pragma: no cover

class Line:  # Mock class to simulate a line# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
 # pragma: no cover
class Feature:  # Mock class to simulate a feature# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
def split_func(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]:  # Mock split function# pragma: no cover
    yield Line([MockLeaf('leaf1')])# pragma: no cover
 # pragma: no cover
class MockLeaf:  # Mock class to represent a leaf# pragma: no cover
    def __init__(self, text):# pragma: no cover
        self.text = text# pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf, inside_brackets):  # Mock function to simulate normalization# pragma: no cover
    leaf.text = f'normalized_{leaf.text}'# pragma: no cover
 # pragma: no cover
line = Line([MockLeaf('original_leaf')])  # Create a mock line with a leaf# pragma: no cover
 # pragma: no cover
features = []  # Initialize features as an empty list# pragma: no cover
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
