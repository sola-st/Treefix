# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_shift.py
# test shift for PeriodIndex
# GH#8083
drange = period_range("20130101", periods=5, freq="D")
result = drange.shift(1)
expected = PeriodIndex(
    ["2013-01-02", "2013-01-03", "2013-01-04", "2013-01-05", "2013-01-06"],
    freq="D",
)
tm.assert_index_equal(result, expected)
