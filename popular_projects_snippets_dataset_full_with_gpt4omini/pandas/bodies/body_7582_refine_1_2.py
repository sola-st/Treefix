import pandas as pd # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'baz'), ('qux', 'one')]) # pragma: no cover

import pandas as pd # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'baz'), ('qux', 'one')]) # pragma: no cover
class MockIndex:# pragma: no cover
    def __init__(self, index):# pragma: no cover
        self.index = index# pragma: no cover
    # pragma: no cover
    def sortlevel(self, level):# pragma: no cover
        return self.index.sort_values().index, None# pragma: no cover
    # pragma: no cover
    def slice_locs(self, start=None, end=None):# pragma: no cover
        start_loc = 0 if start is None else self.index.get_loc(start)# pragma: no cover
        end_loc = len(self.index) if end is None else self.index.get_loc(end)# pragma: no cover
        return start_loc, end_loc# pragma: no cover
# pragma: no cover
sorted_idx = MockIndex(idx) # pragma: no cover

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
