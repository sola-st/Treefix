# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
dr = date_range("2011/1/1", "2012/1/1", freq="W-FRI")
dr_tz = dr.tz_localize(tzstr)

result = dr_tz.shift(1, "10T")
assert result.tz == dr_tz.tz
