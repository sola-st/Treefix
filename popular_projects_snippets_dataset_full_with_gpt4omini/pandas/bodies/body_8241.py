# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
# test shift for DatetimeIndex and non DatetimeIndex
# GH#8083
drange = date_range("20130101", periods=5)
result = drange.shift(1)
expected = DatetimeIndex(
    ["2013-01-02", "2013-01-03", "2013-01-04", "2013-01-05", "2013-01-06"],
    freq="D",
)
tm.assert_index_equal(result, expected)

result = drange.shift(-1)
expected = DatetimeIndex(
    ["2012-12-31", "2013-01-01", "2013-01-02", "2013-01-03", "2013-01-04"],
    freq="D",
)
tm.assert_index_equal(result, expected)

result = drange.shift(3, freq="2D")
expected = DatetimeIndex(
    ["2013-01-07", "2013-01-08", "2013-01-09", "2013-01-10", "2013-01-11"],
    freq="D",
)
tm.assert_index_equal(result, expected)
