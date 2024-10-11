# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
org = date_range(start="2001/02/01 09:00", freq=freq, periods=1)
idx = DatetimeIndex(org, freq=freq)
tm.assert_index_equal(idx, org)

org = date_range(
    start="2001/02/01 09:00", freq=freq, tz="US/Pacific", periods=1
)
idx = DatetimeIndex(org, freq=freq, tz="US/Pacific")
tm.assert_index_equal(idx, org)
