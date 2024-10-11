import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'two'), ('bar', 'one'), ('bar', 'two'), ('baz', 'one'), ('qux', 'one'), ('qux', 'two'), ('qux', 'three')], names=['first', 'second']) # pragma: no cover

import pandas as pd # pragma: no cover

class MockMultiIndex(pd.MultiIndex): # pragma: no cover
    def sortlevel(self, level=0): # pragma: no cover
        sorted_tuples = sorted(self, key=lambda x: x[level]) # pragma: no cover
        sorted_idx = pd.MultiIndex.from_tuples(sorted_tuples, names=self.names) # pragma: no cover
        return sorted_idx, None # pragma: no cover
    def slice_locs(self, start=None, end=None): # pragma: no cover
        def match_key(key): # pragma: no cover
            if key is None: # pragma: no cover
                return True # pragma: no cover
            return lambda x: all(k is None or k == y for k, y in zip(key, x)) # pragma: no cover
        start_key = match_key(start) # pragma: no cover
        end_key = match_key(end) # pragma: no cover
        start_idx = next((i for i, v in enumerate(self) if start_key(v)), 0) # pragma: no cover
        end_idx = next((i for i, v in enumerate(self) if end_key(v)), len(self)) # pragma: no cover
        return start_idx, end_idx # pragma: no cover
idx = MockMultiIndex.from_tuples([('foo', 'two'), ('bar', 'one'), ('bar', 'two'), ('baz', 'one'), ('qux', 'one')], names=['first', 'second']) # pragma: no cover

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
