# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
def check(value):
    # that we are int
    assert isinstance(value, int)

# compat to datetime.timedelta
rng = to_timedelta("1 days, 10:11:12")
assert rng.days == 1
assert rng.seconds == 10 * 3600 + 11 * 60 + 12
assert rng.microseconds == 0
assert rng.nanoseconds == 0

msg = "'Timedelta' object has no attribute '{}'"
with pytest.raises(AttributeError, match=msg.format("hours")):
    rng.hours
with pytest.raises(AttributeError, match=msg.format("minutes")):
    rng.minutes
with pytest.raises(AttributeError, match=msg.format("milliseconds")):
    rng.milliseconds

# GH 10050
check(rng.days)
check(rng.seconds)
check(rng.microseconds)
check(rng.nanoseconds)

td = Timedelta("-1 days, 10:11:12")
assert abs(td) == Timedelta("13:48:48")
assert str(td) == "-1 days +10:11:12"
assert -td == Timedelta("0 days 13:48:48")
assert -Timedelta("-1 days, 10:11:12").value == 49728000000000
assert Timedelta("-1 days, 10:11:12").value == -49728000000000

rng = to_timedelta("-1 days, 10:11:12.100123456")
assert rng.days == -1
assert rng.seconds == 10 * 3600 + 11 * 60 + 12
assert rng.microseconds == 100 * 1000 + 123
assert rng.nanoseconds == 456
msg = "'Timedelta' object has no attribute '{}'"
with pytest.raises(AttributeError, match=msg.format("hours")):
    rng.hours
with pytest.raises(AttributeError, match=msg.format("minutes")):
    rng.minutes
with pytest.raises(AttributeError, match=msg.format("milliseconds")):
    rng.milliseconds

# components
tup = to_timedelta(-1, "us").components
assert tup.days == -1
assert tup.hours == 23
assert tup.minutes == 59
assert tup.seconds == 59
assert tup.milliseconds == 999
assert tup.microseconds == 999
assert tup.nanoseconds == 0

# GH 10050
check(tup.days)
check(tup.hours)
check(tup.minutes)
check(tup.seconds)
check(tup.milliseconds)
check(tup.microseconds)
check(tup.nanoseconds)

tup = Timedelta("-1 days 1 us").components
assert tup.days == -2
assert tup.hours == 23
assert tup.minutes == 59
assert tup.seconds == 59
assert tup.milliseconds == 999
assert tup.microseconds == 999
assert tup.nanoseconds == 0
