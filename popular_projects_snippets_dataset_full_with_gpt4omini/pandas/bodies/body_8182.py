# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("1/1/2011", periods=100, freq="H")

conv = rng.tz_localize("US/Pacific")
exp = date_range("1/1/2011", periods=100, freq="H", tz="US/Pacific")

tm.assert_index_equal(conv, exp._with_freq(None))
