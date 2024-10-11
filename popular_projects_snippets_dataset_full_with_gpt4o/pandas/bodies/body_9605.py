# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
ser = pd.Series([0.1, 0.2, 0.1, pd.NA], dtype="Float64")
result = ser.value_counts(normalize=True)
expected = pd.Series([2, 1], index=ser[:2], dtype="Float64") / 3
assert expected.index.dtype == ser.dtype
tm.assert_series_equal(result, expected)
