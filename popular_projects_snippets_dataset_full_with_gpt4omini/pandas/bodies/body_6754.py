# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
index = self.create_index(closed=closed)
assert index.hasnans is False

result = index.isna()
expected = np.zeros(len(index), dtype=bool)
tm.assert_numpy_array_equal(result, expected)

result = index.notna()
expected = np.ones(len(index), dtype=bool)
tm.assert_numpy_array_equal(result, expected)

index = self.create_index_with_nan(closed=closed)
assert index.hasnans is True

result = index.isna()
expected = np.array([False, True] + [False] * (len(index) - 2))
tm.assert_numpy_array_equal(result, expected)

result = index.notna()
expected = np.array([True, False] + [True] * (len(index) - 2))
tm.assert_numpy_array_equal(result, expected)
