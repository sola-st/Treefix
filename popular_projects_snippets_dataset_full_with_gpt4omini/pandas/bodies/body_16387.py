# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#42137
result = Series([True, False, True, pd.NA], dtype="Int64")
expected = Series([1, 0, 1, pd.NA], dtype="Int64")
tm.assert_series_equal(result, expected)

result = Series([True, False, True], dtype="Int64")
expected = Series([1, 0, 1], dtype="Int64")
tm.assert_series_equal(result, expected)
