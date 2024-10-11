from typing import Iterator, Collection # pragma: no cover
from functools import wraps # pragma: no cover

class Line:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves # pragma: no cover
class Feature:# pragma: no cover
    pass # pragma: no cover
def split_func(line: Line, features: Collection[Feature]) -> Iterator[Line]:# pragma: no cover
    # Mock split function that returns the input line as a list# pragma: no cover
    return [line] # pragma: no cover
def normalize_prefix(leaf, inside_brackets=False):# pragma: no cover
    # Mock normalization function that does nothing# pragma: no cover
    pass # pragma: no cover

from typing import Iterator, Collection # pragma: no cover
from functools import wraps # pragma: no cover

class Line:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves # pragma: no cover
class Feature:# pragma: no cover
    pass # pragma: no cover
def split_func(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]:# pragma: no cover
    # Mock split function that returns the input line as a list# pragma: no cover
    return [line] # pragma: no cover
def normalize_prefix(leaf, inside_brackets=False):# pragma: no cover
    # Mock normalization function for testing# pragma: no cover
    leaf.normalized = True# pragma: no cover
    return leaf # pragma: no cover

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
