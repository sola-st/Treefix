# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
data = [Period("2000", "D"), Period("2001", "D"), None]
result = Series(data_constructor(data))
expected = Series(period_array(data))
tm.assert_series_equal(result, expected)
assert result.dtype == "Period[D]"
