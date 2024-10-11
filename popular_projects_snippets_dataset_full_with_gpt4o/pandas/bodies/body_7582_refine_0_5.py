import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('baz', 'two'), ('qux', 'one'), ('qux', 'two')], names=['first', 'second']) # pragma: no cover
idx.sortlevel = type('Mock', (object,), {'__call__': lambda self, level: (idx.sort_values(), None)})() # pragma: no cover

import pandas as pd # pragma: no cover

idx = pd.MultiIndex.from_tuples([('bar', 'one'), ('bar', 'two'), ('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')], names=['first', 'second']) # pragma: no cover
class Mock:# pragma: no cover
    def sortlevel(self, level):# pragma: no cover
        return (idx, None)# pragma: no cover
idx.sortlevel = Mock().sortlevel # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
from l3.Runtime import _l_
sorted_idx, _ = idx.sortlevel(0)
_l_(20735)

result = sorted_idx.slice_locs(("foo", "two"), ("qux", "one"))
_l_(20736)
assert result == (1, 5)
_l_(20737)

result = sorted_idx.slice_locs(None, ("qux", "one"))
_l_(20738)
assert result == (0, 5)
_l_(20739)

result = sorted_idx.slice_locs(("foo", "two"), None)
_l_(20740)
assert result == (1, len(sorted_idx))
_l_(20741)

result = sorted_idx.slice_locs("bar", "baz")
_l_(20742)
assert result == (2, 4)
_l_(20743)
