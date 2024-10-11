# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
expected = np.timedelta64(10, "D").astype("m8[ns]").view("i8")
assert Timedelta(10, unit="d").value == expected
assert Timedelta(10.0, unit="d").value == expected
assert Timedelta("10 days").value == expected
assert Timedelta(days=10).value == expected
assert Timedelta(days=10.0).value == expected

expected += np.timedelta64(10, "s").astype("m8[ns]").view("i8")
assert Timedelta("10 days 00:00:10").value == expected
assert Timedelta(days=10, seconds=10).value == expected
assert Timedelta(days=10, milliseconds=10 * 1000).value == expected
assert Timedelta(days=10, microseconds=10 * 1000 * 1000).value == expected

# rounding cases
assert Timedelta(82739999850000).value == 82739999850000
assert "0 days 22:58:59.999850" in str(Timedelta(82739999850000))
assert Timedelta(123072001000000).value == 123072001000000
assert "1 days 10:11:12.001" in str(Timedelta(123072001000000))

# string conversion with/without leading zero
# GH#9570
assert Timedelta("0:00:00") == timedelta(hours=0)
assert Timedelta("00:00:00") == timedelta(hours=0)
assert Timedelta("-1:00:00") == -timedelta(hours=1)
assert Timedelta("-01:00:00") == -timedelta(hours=1)

# more strings & abbrevs
# GH#8190
assert Timedelta("1 h") == timedelta(hours=1)
assert Timedelta("1 hour") == timedelta(hours=1)
assert Timedelta("1 hr") == timedelta(hours=1)
assert Timedelta("1 hours") == timedelta(hours=1)
assert Timedelta("-1 hours") == -timedelta(hours=1)
assert Timedelta("1 m") == timedelta(minutes=1)
assert Timedelta("1.5 m") == timedelta(seconds=90)
assert Timedelta("1 minute") == timedelta(minutes=1)
assert Timedelta("1 minutes") == timedelta(minutes=1)
assert Timedelta("1 s") == timedelta(seconds=1)
assert Timedelta("1 second") == timedelta(seconds=1)
assert Timedelta("1 seconds") == timedelta(seconds=1)
assert Timedelta("1 ms") == timedelta(milliseconds=1)
assert Timedelta("1 milli") == timedelta(milliseconds=1)
assert Timedelta("1 millisecond") == timedelta(milliseconds=1)
assert Timedelta("1 us") == timedelta(microseconds=1)
assert Timedelta("1 µs") == timedelta(microseconds=1)
assert Timedelta("1 micros") == timedelta(microseconds=1)
assert Timedelta("1 microsecond") == timedelta(microseconds=1)
assert Timedelta("1.5 microsecond") == Timedelta("00:00:00.000001500")
assert Timedelta("1 ns") == Timedelta("00:00:00.000000001")
assert Timedelta("1 nano") == Timedelta("00:00:00.000000001")
assert Timedelta("1 nanosecond") == Timedelta("00:00:00.000000001")

# combos
assert Timedelta("10 days 1 hour") == timedelta(days=10, hours=1)
assert Timedelta("10 days 1 h") == timedelta(days=10, hours=1)
assert Timedelta("10 days 1 h 1m 1s") == timedelta(
    days=10, hours=1, minutes=1, seconds=1
)
assert Timedelta("-10 days 1 h 1m 1s") == -timedelta(
    days=10, hours=1, minutes=1, seconds=1
)
assert Timedelta("-10 days 1 h 1m 1s") == -timedelta(
    days=10, hours=1, minutes=1, seconds=1
)
assert Timedelta("-10 days 1 h 1m 1s 3us") == -timedelta(
    days=10, hours=1, minutes=1, seconds=1, microseconds=3
)
assert Timedelta("-10 days 1 h 1.5m 1s 3us") == -timedelta(
    days=10, hours=1, minutes=1, seconds=31, microseconds=3
)

# Currently invalid as it has a - on the hh:mm:dd part
# (only allowed on the days)
msg = "only leading negative signs are allowed"
with pytest.raises(ValueError, match=msg):
    Timedelta("-10 days -1 h 1.5m 1s 3us")

# only leading neg signs are allowed
with pytest.raises(ValueError, match=msg):
    Timedelta("10 days -1 h 1.5m 1s 3us")

# no units specified
msg = "no units specified"
with pytest.raises(ValueError, match=msg):
    Timedelta("3.1415")

# invalid construction
msg = "cannot construct a Timedelta"
with pytest.raises(ValueError, match=msg):
    Timedelta()

msg = "unit abbreviation w/o a number"
with pytest.raises(ValueError, match=msg):
    Timedelta("foo")

msg = (
    "cannot construct a Timedelta from "
    "the passed arguments, allowed keywords are "
)
with pytest.raises(ValueError, match=msg):
    Timedelta(day=10)

# floats
expected = np.timedelta64(10, "s").astype("m8[ns]").view("i8") + np.timedelta64(
    500, "ms"
).astype("m8[ns]").view("i8")
assert Timedelta(10.5, unit="s").value == expected

# offset
assert to_timedelta(offsets.Hour(2)) == Timedelta(hours=2)
assert Timedelta(offsets.Hour(2)) == Timedelta(hours=2)
assert Timedelta(offsets.Second(2)) == Timedelta(seconds=2)

# GH#11995: unicode
expected = Timedelta("1H")
result = Timedelta("1H")
assert result == expected
assert to_timedelta(offsets.Hour(2)) == Timedelta("0 days, 02:00:00")

msg = "unit abbreviation w/o a number"
with pytest.raises(ValueError, match=msg):
    Timedelta("foo bar")
