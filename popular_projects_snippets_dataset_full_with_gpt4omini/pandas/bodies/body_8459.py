# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
# GH 6538: Check that DatetimeIndex and its TimeStamp elements
# return the same weekofyear accessor close to new year w/ tz
dates = ["2013/12/29", "2013/12/30", "2013/12/31"]
dates = DatetimeIndex(dates, tz="Europe/Brussels")
expected = [52, 1, 1]
assert dates.isocalendar().week.tolist() == expected
assert [d.weekofyear for d in dates] == expected
