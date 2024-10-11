# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_setops.py
# GH#38302
idx = period_range("2011-01-01", periods=2)
idx_dup = idx.append(idx)
result = idx_dup.intersection(idx_dup)
tm.assert_index_equal(result, idx)
