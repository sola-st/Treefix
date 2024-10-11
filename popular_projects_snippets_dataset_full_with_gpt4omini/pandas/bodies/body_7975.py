# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
for freq in ["1D1H", "1H1D"]:
    pidx = PeriodIndex(["2016-01-01", "2016-01-02"], freq=freq)
    expected = PeriodIndex(["2016-01-01 00:00", "2016-01-02 00:00"], freq="25H")
for freq in ["1D1H", "1H1D"]:
    pidx = period_range(start="2016-01-01", periods=2, freq=freq)
    expected = PeriodIndex(["2016-01-01 00:00", "2016-01-02 01:00"], freq="25H")
    tm.assert_index_equal(pidx, expected)
