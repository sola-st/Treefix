# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# round
ser = Series(
    pd.to_datetime(
        ["2012-01-01 13:00:00", "2012-01-01 12:01:00", "2012-01-01 08:00:00"]
    ),
    name="xxx",
)
result = getattr(ser.dt, method)("D")
expected = Series(pd.to_datetime(dates), name="xxx")
tm.assert_series_equal(result, expected)
