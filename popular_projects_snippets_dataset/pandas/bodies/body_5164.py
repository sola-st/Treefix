# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GG#33441
arr = np.arange(5).astype("timedelta64[ns]")
td = Timedelta(arr[1])

expected = np.array([False, True, False, False, False], dtype=bool)

result = td == arr
tm.assert_numpy_array_equal(result, expected)

result = arr == td
tm.assert_numpy_array_equal(result, expected)

result = td != arr
tm.assert_numpy_array_equal(result, ~expected)

result = arr != td
tm.assert_numpy_array_equal(result, ~expected)
