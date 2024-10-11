# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# GH#33573
tz = tz_naive_fixture
dti = DatetimeIndex([], tz=tz, freq="D")
item = Timestamp("2017-04-05").tz_localize(tz)

result = dti.insert(0, item)
assert result.freq == dti.freq

# But not when we insert an item that doesn't conform to freq
dti = DatetimeIndex([], tz=tz, freq="W-THU")
result = dti.insert(0, item)
assert result.freq is None
