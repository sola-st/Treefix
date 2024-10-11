# Extracted from ./data/repos/pandas/pandas/tests/window/test_cython_aggregations.py
# GH-45647
minp, step, width, size, selection = 0, 1, 3, 11, [2, 7]
values = np.arange(1, 1 + size, dtype=np.float64)
end = np.arange(width, size, step, dtype=np.int64)
start = end - width
selarr = np.array(selection, dtype=np.int32)
result = Series(rolling_aggregation(values, start[selarr], end[selarr], minp))
expected = Series(rolling_aggregation(values, start, end, minp)[selarr])
tm.assert_equal(expected, result)
