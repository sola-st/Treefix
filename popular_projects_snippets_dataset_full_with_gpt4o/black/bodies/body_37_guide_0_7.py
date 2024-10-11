from functools import wraps # pragma: no cover
from typing import Collection, Iterator # pragma: no cover
import sys # pragma: no cover

split_func = lambda line, features: [type('Line', (object,), {'leaves': [type('Leaf', (object,), {'text': 'example'})()]})()] # pragma: no cover
normalize_prefix = lambda leaf, inside_brackets: None # pragma: no cover
Line = type('Line', (object,), {'leaves': [type('Leaf', (object,), {'text': 'example'})()]}) # pragma: no cover
Feature = type('Feature', (object,), {}) # pragma: no cover
sys.exit = lambda x=None: print('Exit called') # pragma: no cover

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
