# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_join.py
joined = idx.join(idx, how=join_type)
tm.assert_index_equal(joined, idx)
