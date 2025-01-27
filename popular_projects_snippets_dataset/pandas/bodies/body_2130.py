# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
ts_strings = ["2015-11-18 15:30:00+05:30", "2015-11-18 16:30:00+06:30", NaT]
result = to_datetime(ts_strings, utc=True)
expected = DatetimeIndex(
    [Timestamp(2015, 11, 18, 10), Timestamp(2015, 11, 18, 10), NaT], tz="UTC"
)
tm.assert_index_equal(result, expected)
