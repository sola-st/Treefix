# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
strdates = ["1/1/2012", "3/1/2012", "4/1/2012"]
idx = DatetimeIndex(strdates, tz=prefix + "US/Eastern")

conv = idx[0].tz_convert(prefix + "US/Pacific")
expected = idx.tz_convert(prefix + "US/Pacific")[0]

assert conv == expected
