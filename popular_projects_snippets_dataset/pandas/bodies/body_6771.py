# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
index = self.create_index(closed=closed)

expected = np.array([True] + [False] * (len(index) - 1))
result = index.isin(index[:1])
tm.assert_numpy_array_equal(result, expected)

result = index.isin([index[0]])
tm.assert_numpy_array_equal(result, expected)

other = IntervalIndex.from_breaks(np.arange(-2, 10), closed=closed)
expected = np.array([True] * (len(index) - 1) + [False])
result = index.isin(other)
tm.assert_numpy_array_equal(result, expected)

result = index.isin(other.tolist())
tm.assert_numpy_array_equal(result, expected)

for other_closed in ["right", "left", "both", "neither"]:
    other = self.create_index(closed=other_closed)
    expected = np.repeat(closed == other_closed, len(index))
    result = index.isin(other)
    tm.assert_numpy_array_equal(result, expected)

    result = index.isin(other.tolist())
    tm.assert_numpy_array_equal(result, expected)
