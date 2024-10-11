# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# case where we are going neither to nor from nano
ts = Timestamp("1970-01-02").as_unit("ms")
assert ts.year == 1970
assert ts.month == 1
assert ts.day == 2
assert ts.hour == ts.minute == ts.second == ts.microsecond == ts.nanosecond == 0

res = ts.as_unit("s")
assert res.value == 24 * 3600
assert res.year == 1970
assert res.month == 1
assert res.day == 2
assert (
    res.hour
    == res.minute
    == res.second
    == res.microsecond
    == res.nanosecond
    == 0
)
