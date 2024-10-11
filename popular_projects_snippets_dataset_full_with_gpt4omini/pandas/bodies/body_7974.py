# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
freqstr = str(mult) + freq
pidx = period_range(start="2014-04-01", freq=freqstr, periods=10)
expected = date_range(start="2014-04-01", freq=freqstr, periods=10).to_period(
    freqstr
)
tm.assert_index_equal(pidx, expected)
