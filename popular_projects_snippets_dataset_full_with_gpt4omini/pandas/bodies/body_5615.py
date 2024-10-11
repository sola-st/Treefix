# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

arr = date_range("20130101", periods=3).values
result = algos.isin(arr, [arr[0]])
expected = np.array([True, False, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(arr, arr[0:2])
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(arr, set(arr[0:2]))
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)

arr = timedelta_range("1 day", periods=3).values
result = algos.isin(arr, [arr[0]])
expected = np.array([True, False, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(arr, arr[0:2])
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(arr, set(arr[0:2]))
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)
