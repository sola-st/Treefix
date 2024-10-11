# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 32621, GH#44940
ser = pd.Series(["one", "two", np.nan], dtype=nullable_string_dtype)
expected = pd.Series(["1", "2", np.nan], dtype=nullable_string_dtype)
result = ser.replace({"one": "1", "two": "2"})
tm.assert_series_equal(expected, result)
