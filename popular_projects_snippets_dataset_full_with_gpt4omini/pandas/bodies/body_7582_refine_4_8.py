import pandas as pd # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'baz'), ('qux', 'one'), ('qux', 'two')]) # pragma: no cover
class Mock: pass # pragma: no cover
idx.sortlevel = lambda level: (idx.sort_values(level), None) # pragma: no cover

import pandas as pd # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'baz'), ('qux', 'one'), ('qux', 'two')], names=['first', 'second']) # pragma: no cover
sorted_idx = idx.sortlevel(0)[0] # pragma: no cover
def slice_locs(start, end): # pragma: no cover
    return sorted_idx.get_loc(start), sorted_idx.get_loc(end, method='bfill') # pragma: no cover
sorted_idx.slice_locs = slice_locs # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
from l3.Runtime import _l_
sorted_idx, _ = idx.sortlevel(0)
_l_(9961)

result = sorted_idx.slice_locs(("foo", "two"), ("qux", "one"))
_l_(9962)
assert result == (1, 5)
_l_(9963)

result = sorted_idx.slice_locs(None, ("qux", "one"))
_l_(9964)
assert result == (0, 5)
_l_(9965)

result = sorted_idx.slice_locs(("foo", "two"), None)
_l_(9966)
assert result == (1, len(sorted_idx))
_l_(9967)

result = sorted_idx.slice_locs("bar", "baz")
_l_(9968)
assert result == (2, 4)
_l_(9969)
