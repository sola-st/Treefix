# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
ser = pd.Series(["a", "b", "a", pd.NA], dtype=dtype)
result = ser.value_counts(normalize=True)
expected = pd.Series([2, 1], index=ser[:2], dtype="Float64") / 3
tm.assert_series_equal(result, expected)
