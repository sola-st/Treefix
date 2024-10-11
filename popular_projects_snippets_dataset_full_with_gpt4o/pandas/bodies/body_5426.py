# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
stamp = Timestamp(value, unit=unit)
assert stamp.year == 2000
assert stamp.month == 1
assert stamp.day == 1
assert stamp.hour == h
if unit != "D":
    assert stamp.minute == 1
    assert stamp.second == s
    assert stamp.microsecond == us
else:
    assert stamp.minute == 0
    assert stamp.second == 0
    assert stamp.microsecond == 0
assert stamp.nanosecond == ns
