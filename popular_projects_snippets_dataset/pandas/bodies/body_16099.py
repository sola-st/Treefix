# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 27952
datetimes = Series(
    ["2018-01-01", "2018-01-01", "2019-01-02"], dtype="datetime64[ns]"
)
categorical = datetimes.astype("category")
result = getattr(categorical.dt, accessor)
expected = getattr(datetimes.dt, accessor)
tm.assert_series_equal(result, expected)
