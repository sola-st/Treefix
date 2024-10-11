# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 27952
tz = tz_aware_fixture
datetimes = Series(
    ["2019-01-01", "2019-01-01", "2019-01-02"], dtype="datetime64[ns]"
)
categorical = datetimes.astype("category")
result = categorical.dt.tz_localize(tz)
expected = datetimes.dt.tz_localize(tz)
tm.assert_series_equal(result, expected)
