from typing import Collection, Iterator # pragma: no cover
from functools import wraps # pragma: no cover
from collections.abc import Iterator as AbsIterator # pragma: no cover

class Line: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
class Feature: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def wrap_func(func): # pragma: no cover
    @wraps(func) # pragma: no cover
    def wrapper(*args, **kwargs): # pragma: no cover
        return func(*args, **kwargs) # pragma: no cover
    return wrapper # pragma: no cover
 # pragma: no cover
def split_func(line: Line, features: Collection[Feature]) -> Iterator[Line]: # pragma: no cover
    yield line # pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf, inside_brackets: bool): # pragma: no cover
    pass # pragma: no cover

from typing import Collection, Iterator, List # pragma: no cover
from functools import wraps # pragma: no cover

class Line: # pragma: no cover
    def __init__(self, leaves: List[str]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
class Feature: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def split_func(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]: # pragma: no cover
    # Assuming split_func should split leaves into individual lines # pragma: no cover
    for leaf in line.leaves: # pragma: no cover
        yield Line([leaf]) # pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf: str, inside_brackets: bool = False): # pragma: no cover
    # Placeholder function for normalizing prefix # pragma: no cover
    pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Normalize prefix of the first leaf in every line returned by `split_func`.

    This is a decorator over relevant split functions.
    """

@wraps(split_func)
def split_wrapper(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]:
    _l_(18599)

    for split_line in split_func(line, features):
        _l_(18598)

        normalize_prefix(split_line.leaves[0], inside_brackets=True)
        _l_(18596)
        aux = split_line
        _l_(18597)
        exit(aux)
aux = split_wrapper
_l_(18600)

exit(aux)
