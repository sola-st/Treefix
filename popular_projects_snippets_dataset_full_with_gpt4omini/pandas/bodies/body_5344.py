# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# GH#31475 Avoid floating point errors dropping the start_time to
#  before the beginning of the Period
per = Period("2020-01-30 15:57:27.576166", freq="U")
assert per.ordinal == 1580399847576166

start = per.start_time
expected = Timestamp("2020-01-30 15:57:27.576166")
assert start == expected
assert start.value == per.ordinal * 1000

per2 = Period("2300-01-01", "us")
msg = "2300-01-01"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    per2.start_time
with pytest.raises(OutOfBoundsDatetime, match=msg):
    per2.end_time
