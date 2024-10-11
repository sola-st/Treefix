# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
# GH#14811
idx = simple_index[:0]
tm.assert_index_equal(idx, idx.shift(1))
