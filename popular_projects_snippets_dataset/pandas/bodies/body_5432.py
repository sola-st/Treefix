# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH 7610
expected = 1_293_840_000_000_000_005
t = Timestamp("2011-01-01") + offsets.Nano(5)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
assert t.value == expected
assert t.nanosecond == 5

t = Timestamp(t)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
assert t.value == expected
assert t.nanosecond == 5

t = Timestamp("2011-01-01 00:00:00.000000005")
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
assert t.value == expected
assert t.nanosecond == 5

expected = 1_293_840_000_000_000_010
t = t + offsets.Nano(5)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
assert t.value == expected
assert t.nanosecond == 10

t = Timestamp(t)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
assert t.value == expected
assert t.nanosecond == 10

t = Timestamp("2011-01-01 00:00:00.000000010")
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
assert t.value == expected
assert t.nanosecond == 10
