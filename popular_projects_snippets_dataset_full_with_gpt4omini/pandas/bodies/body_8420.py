# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
tz = timezones.maybe_get_tz(tzstr)
result = date_range("1/1/2000", periods=10, tz=tzstr)
expected = date_range("1/1/2000", periods=10, tz=tz)

tm.assert_index_equal(result, expected)
