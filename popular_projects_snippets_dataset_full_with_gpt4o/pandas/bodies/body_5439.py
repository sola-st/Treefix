# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH#45087
tzstr = "dateutil/usr/share/zoneinfo/America/Chicago"
ts = Timestamp(year=2013, month=11, day=3, hour=1, minute=0, fold=1, tz=tzstr)
dt = ts.to_pydatetime()
assert dt.fold == 1
