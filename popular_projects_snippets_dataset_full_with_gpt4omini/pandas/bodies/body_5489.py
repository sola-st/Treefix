# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
ts = Timestamp("2021-01-01")
ts2 = Timestamp("2019-04-05")
arr = np.array([[ts.asm8, ts2.asm8]], dtype="M8[ns]")

result = ts == arr
expected = np.array([[True, False]], dtype=bool)
tm.assert_numpy_array_equal(result, expected)

result = arr == ts
tm.assert_numpy_array_equal(result, expected)

result = ts != arr
tm.assert_numpy_array_equal(result, ~expected)

result = arr != ts
tm.assert_numpy_array_equal(result, ~expected)

result = ts2 < arr
tm.assert_numpy_array_equal(result, expected)

result = arr < ts2
tm.assert_numpy_array_equal(result, np.array([[False, False]], dtype=bool))

result = ts2 <= arr
tm.assert_numpy_array_equal(result, np.array([[True, True]], dtype=bool))

result = arr <= ts2
tm.assert_numpy_array_equal(result, ~expected)

result = ts >= arr
tm.assert_numpy_array_equal(result, np.array([[True, True]], dtype=bool))

result = arr >= ts
tm.assert_numpy_array_equal(result, np.array([[True, False]], dtype=bool))
