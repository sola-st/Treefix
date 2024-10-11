# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting values in a viewing Series with an indexer
s = Series([1, 2, 3], index=["a", "b", "c"])
s_orig = s.copy()
subset = s[:]

indexer_si(subset)[indexer] = 0
expected = Series([0, 0, 3], index=["a", "b", "c"])
tm.assert_series_equal(subset, expected)

if using_copy_on_write:
    tm.assert_series_equal(s, s_orig)
else:
    tm.assert_series_equal(s, expected)
