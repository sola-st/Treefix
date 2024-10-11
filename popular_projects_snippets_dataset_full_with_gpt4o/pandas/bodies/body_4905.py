# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series(
    ["ABCDEFG", "BCDEFEF", "DEFGHIJEF", "EFGHEF", "XXXX"], dtype=any_string_dtype
)
expected_dtype = np.int64 if any_string_dtype == "object" else "Int64"

result = ser.str.find("EF")
expected = Series([4, 3, 1, 0, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.find("EF") for v in np.array(ser)], dtype=np.int64)
tm.assert_numpy_array_equal(np.array(result, dtype=np.int64), expected)

result = ser.str.rfind("EF")
expected = Series([4, 5, 7, 4, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.rfind("EF") for v in np.array(ser)], dtype=np.int64)
tm.assert_numpy_array_equal(np.array(result, dtype=np.int64), expected)

result = ser.str.find("EF", 3)
expected = Series([4, 3, 7, 4, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.find("EF", 3) for v in np.array(ser)], dtype=np.int64)
tm.assert_numpy_array_equal(np.array(result, dtype=np.int64), expected)

result = ser.str.rfind("EF", 3)
expected = Series([4, 5, 7, 4, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.rfind("EF", 3) for v in np.array(ser)], dtype=np.int64)
tm.assert_numpy_array_equal(np.array(result, dtype=np.int64), expected)

result = ser.str.find("EF", 3, 6)
expected = Series([4, 3, -1, 4, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.find("EF", 3, 6) for v in np.array(ser)], dtype=np.int64)
tm.assert_numpy_array_equal(np.array(result, dtype=np.int64), expected)

result = ser.str.rfind("EF", 3, 6)
expected = Series([4, 3, -1, 4, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.rfind("EF", 3, 6) for v in np.array(ser)], dtype=np.int64)
tm.assert_numpy_array_equal(np.array(result, dtype=np.int64), expected)
