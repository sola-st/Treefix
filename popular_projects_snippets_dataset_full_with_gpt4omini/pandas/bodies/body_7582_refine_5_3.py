import pandas as pd # pragma: no cover

idx = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('bar', 'one'), ('bar', 'baz')], names=['first', 'second']) # pragma: no cover
sorted_idx = idx.sortlevel(0) # pragma: no cover

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
