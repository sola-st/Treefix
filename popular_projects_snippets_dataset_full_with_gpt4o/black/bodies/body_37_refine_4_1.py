from typing import Collection, Iterator # pragma: no cover
from collections.abc import Iterable # pragma: no cover
from functools import wraps # pragma: no cover

class Line: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
class Feature: # pragma: no cover
    pass # pragma: no cover
def split_func(line: Line, features: Collection[Feature]) -> Iterator[Line]: # pragma: no cover
    yield line # pragma: no cover
def normalize_prefix(text, inside_brackets=False): # pragma: no cover
    pass # pragma: no cover

from typing import Collection, Iterator, List # pragma: no cover
from functools import wraps # pragma: no cover

class Line: # pragma: no cover
    def __init__(self, leaves: List[str]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
class Feature: # pragma: no cover
    def __init__(self, name: str): # pragma: no cover
        self.name = name # pragma: no cover
 # pragma: no cover
def split_func(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]: # pragma: no cover
    leaf_prefixes = ['prefix1', 'prefix2'] # pragma: no cover
    for prefix in leaf_prefixes: # pragma: no cover
        new_leaves = [prefix + leaf for leaf in line.leaves] # pragma: no cover
        yield Line(new_leaves) # pragma: no cover
 # pragma: no cover
def normalize_prefix(leaf: str, inside_brackets: bool): # pragma: no cover
    # Normalization logic here # pragma: no cover
    if inside_brackets: # pragma: no cover
        leaf = '[' + leaf + ']' # pragma: no cover

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
