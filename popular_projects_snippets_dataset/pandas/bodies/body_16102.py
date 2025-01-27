# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 10086
ser = Series(date_range("20130101", periods=5))
result = ser.dt.strftime("%Y/%m/%d")
expected = Series(
    ["2013/01/01", "2013/01/02", "2013/01/03", "2013/01/04", "2013/01/05"]
)
tm.assert_series_equal(result, expected)

ser = Series(date_range("2015-02-03 11:22:33.4567", periods=5))
result = ser.dt.strftime("%Y/%m/%d %H-%M-%S")
expected = Series(
    [
        "2015/02/03 11-22-33",
        "2015/02/04 11-22-33",
        "2015/02/05 11-22-33",
        "2015/02/06 11-22-33",
        "2015/02/07 11-22-33",
    ]
)
tm.assert_series_equal(result, expected)

ser = Series(period_range("20130101", periods=5))
result = ser.dt.strftime("%Y/%m/%d")
expected = Series(
    ["2013/01/01", "2013/01/02", "2013/01/03", "2013/01/04", "2013/01/05"]
)
tm.assert_series_equal(result, expected)

ser = Series(period_range("2015-02-03 11:22:33.4567", periods=5, freq="s"))
result = ser.dt.strftime("%Y/%m/%d %H-%M-%S")
expected = Series(
    [
        "2015/02/03 11-22-33",
        "2015/02/03 11-22-34",
        "2015/02/03 11-22-35",
        "2015/02/03 11-22-36",
        "2015/02/03 11-22-37",
    ]
)
tm.assert_series_equal(result, expected)
