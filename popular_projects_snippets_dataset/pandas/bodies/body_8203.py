# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH25241
t3 = DatetimeIndex(["2019-01-01 10:00"], freq="H")
assert t3.tz_localize(tz=tz_naive_fixture).freq == t3.freq
t4 = DatetimeIndex(["2019-01-02 12:00"], tz="UTC", freq="T")
assert t4.tz_convert(tz="UTC").freq == t4.freq
