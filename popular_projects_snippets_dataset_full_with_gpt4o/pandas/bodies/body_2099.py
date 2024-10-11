# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/31491
# Need at least 50 to ensure cache is used.
dts = [
    np.datetime64("2000-01-01", unit),
    np.datetime64("2000-01-02", unit),
] * 30
# Assuming all datetimes are in bounds, to_datetime() returns
# an array that is equal to Timestamp() parsing
result = to_datetime(dts, cache=cache)
expected = DatetimeIndex([Timestamp(x).asm8 for x in dts], dtype="M8[ns]")
tm.assert_index_equal(result, expected)

# A list of datetimes where the last one is out of bounds
dts_with_oob = dts + [np.datetime64("9999-01-01")]

msg = "Out of bounds nanosecond timestamp: 9999-01-01 00:00:00"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(dts_with_oob, errors="raise")

tm.assert_index_equal(
    to_datetime(dts_with_oob, errors="coerce", cache=cache),
    DatetimeIndex(
        [Timestamp(dts_with_oob[0]).asm8, Timestamp(dts_with_oob[1]).asm8] * 30
        + [NaT],
    ),
)

# With errors='ignore', out of bounds datetime64s
# are converted to their .item(), which depending on the version of
# numpy is either a python datetime.datetime or datetime.date
tm.assert_index_equal(
    to_datetime(dts_with_oob, errors="ignore", cache=cache),
    Index([dt.item() for dt in dts_with_oob]),
)
