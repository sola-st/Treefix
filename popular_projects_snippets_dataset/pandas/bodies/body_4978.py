# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Test for uint64 overflow.
s = Series([1, 2**63, 2**63], dtype=np.uint64)
result = s.mode(dropna)
expected1 = Series(expected1, dtype=np.uint64)
tm.assert_series_equal(result, expected1)

s = Series([1, 2**63], dtype=np.uint64)
result = s.mode(dropna)
expected2 = Series(expected2, dtype=np.uint64)
tm.assert_series_equal(result, expected2)
