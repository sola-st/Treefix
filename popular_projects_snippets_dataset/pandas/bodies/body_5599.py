# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 9431
expected = np.array([31200, 45678, 10000], dtype="m8[ns]")

td_index = to_timedelta([31200, 45678, 31200, 10000, 45678])
result = algos.unique(td_index)
tm.assert_numpy_array_equal(result, expected)
assert result.dtype == expected.dtype

s = Series(td_index)
result = algos.unique(s)
tm.assert_numpy_array_equal(result, expected)
assert result.dtype == expected.dtype

arr = s.values
result = algos.unique(arr)
tm.assert_numpy_array_equal(result, expected)
assert result.dtype == expected.dtype
