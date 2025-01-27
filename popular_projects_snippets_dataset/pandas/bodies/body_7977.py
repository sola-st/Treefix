# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
org = period_range(start="2001/04/01", freq=freq, periods=1)
idx = PeriodIndex(org.values, freq=freq)
tm.assert_index_equal(idx, org)
