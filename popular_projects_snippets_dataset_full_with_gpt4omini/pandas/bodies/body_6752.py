# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
index = self.create_index(closed=closed)
assert len(index) == 10
assert index.size == 10
assert index.shape == (10,)

tm.assert_index_equal(index.left, Index(np.arange(10, dtype=np.int64)))
tm.assert_index_equal(index.right, Index(np.arange(1, 11, dtype=np.int64)))
tm.assert_index_equal(index.mid, Index(np.arange(0.5, 10.5, dtype=np.float64)))

assert index.closed == closed

ivs = [
    Interval(left, right, closed)
    for left, right in zip(range(10), range(1, 11))
]
expected = np.array(ivs, dtype=object)
tm.assert_numpy_array_equal(np.asarray(index), expected)

# with nans
index = self.create_index_with_nan(closed=closed)
assert len(index) == 10
assert index.size == 10
assert index.shape == (10,)

expected_left = Index([0, np.nan, 2, 3, 4, 5, 6, 7, 8, 9])
expected_right = expected_left + 1
expected_mid = expected_left + 0.5
tm.assert_index_equal(index.left, expected_left)
tm.assert_index_equal(index.right, expected_right)
tm.assert_index_equal(index.mid, expected_mid)

assert index.closed == closed

ivs = [
    Interval(left, right, closed) if notna(left) else np.nan
    for left, right in zip(expected_left, expected_right)
]
expected = np.array(ivs, dtype=object)
tm.assert_numpy_array_equal(np.asarray(index), expected)
