# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 41047
ser = Series([ts + zero_tz])
result = to_datetime(ser)
tz = pytz.utc if zero_tz == "Z" else None
expected = Series([Timestamp(ts, tz=tz)])
tm.assert_series_equal(result, expected)
