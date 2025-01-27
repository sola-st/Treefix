# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 11018
rng = date_range("2011-12-31", freq="-2A", periods=3)
exp = DatetimeIndex(["2011-12-31", "2009-12-31", "2007-12-31"], freq="-2A")
tm.assert_index_equal(rng, exp)
assert rng.freq == "-2A"

rng = date_range("2011-01-31", freq="-2M", periods=3)
exp = DatetimeIndex(["2011-01-31", "2010-11-30", "2010-09-30"], freq="-2M")
tm.assert_index_equal(rng, exp)
assert rng.freq == "-2M"
