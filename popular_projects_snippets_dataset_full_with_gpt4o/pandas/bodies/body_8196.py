# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("03/12/2012 00:00", periods=10, freq="W-FRI", tz="US/Eastern")
rng2 = DatetimeIndex(data=rng, tz="US/Eastern")
tm.assert_index_equal(rng, rng2)
