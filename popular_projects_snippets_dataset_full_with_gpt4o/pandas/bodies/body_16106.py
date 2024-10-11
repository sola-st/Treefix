# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
ser = Series(period_range("20130101", periods=4, freq="H"))
result = ser.dt.strftime("%Y/%m/%d %H:%M:%S")
expected = Series(
    [
        "2013/01/01 00:00:00",
        "2013/01/01 01:00:00",
        "2013/01/01 02:00:00",
        "2013/01/01 03:00:00",
    ]
)
tm.assert_series_equal(result, expected)
