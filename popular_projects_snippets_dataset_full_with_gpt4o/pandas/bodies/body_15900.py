# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_values.py
tm.assert_almost_equal(
    datetime_series.values, datetime_series, check_dtype=False
)
