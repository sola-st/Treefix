# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 35297
timezone = warsaw

# nonexistent keyword in start
start = Timestamp("2015-03-29 02:30:00").tz_localize(
    timezone, nonexistent="shift_forward"
)
result = date_range(start=start, periods=2, freq="H")
expected = DatetimeIndex(
    [
        Timestamp("2015-03-29 03:00:00+02:00", tz=timezone),
        Timestamp("2015-03-29 04:00:00+02:00", tz=timezone),
    ]
)

tm.assert_index_equal(result, expected)

# nonexistent keyword in end
end = Timestamp("2015-03-29 02:30:00").tz_localize(
    timezone, nonexistent="shift_forward"
)
result = date_range(end=end, periods=2, freq="H")
expected = DatetimeIndex(
    [
        Timestamp("2015-03-29 01:00:00+01:00", tz=timezone),
        Timestamp("2015-03-29 03:00:00+02:00", tz=timezone),
    ]
)

tm.assert_index_equal(result, expected)
