# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
ser = Series(period_range("20130101", periods=4, freq="L"))
result = ser.dt.strftime("%Y/%m/%d %H:%M:%S.%l")
expected = Series(
    [
        "2013/01/01 00:00:00.000",
        "2013/01/01 00:00:00.001",
        "2013/01/01 00:00:00.002",
        "2013/01/01 00:00:00.003",
    ]
)
tm.assert_series_equal(result, expected)
