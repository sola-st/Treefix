# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#2621
ind = date_range("2012-12-01", periods=10, tz="utc")
ind = ind.drop(ind[-1])

assert ind.tz is not None
