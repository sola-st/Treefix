# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
ser = Series(["a", "b", np.nan, "c", "a"])

result = ser == "a"
expected = Series([True, False, False, False, True])
tm.assert_series_equal(result, expected)

result = ser < "a"
expected = Series([False, False, False, False, False])
tm.assert_series_equal(result, expected)

result = ser != "a"
expected = -(ser == "a")
tm.assert_series_equal(result, expected)
