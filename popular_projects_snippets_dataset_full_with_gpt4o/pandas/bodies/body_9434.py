# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
# GH 33172
ser = pd.Series([1, 2, 1, pd.NA], dtype="Int64")
result = ser.value_counts(normalize=True)
expected = pd.Series([2, 1], index=ser[:2], dtype="Float64") / 3
assert expected.index.dtype == ser.dtype
tm.assert_series_equal(result, expected)
