# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_function.py
ser = pd.Series([True, False, pd.NA], dtype="boolean")
result = ser.value_counts(normalize=True)
expected = pd.Series([1, 1], index=ser[:-1], dtype="Float64") / 2
assert expected.index.dtype == "boolean"
tm.assert_series_equal(result, expected)
