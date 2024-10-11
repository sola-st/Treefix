# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py

idx = simple_index
tm.assert_index_equal(idx, idx.shift(0))
