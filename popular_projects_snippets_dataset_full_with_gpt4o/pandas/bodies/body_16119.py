# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#21205
expected = Series([input_vals], dtype="Period[D]")
result = Series([input_vals], dtype="datetime64[ns]").dt.to_period("D")
tm.assert_series_equal(result, expected)
