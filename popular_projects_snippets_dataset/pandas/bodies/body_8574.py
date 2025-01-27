# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 20854
ts = [
    Timestamp("2016-10-30 03:00:00+0300", tz="Europe/Helsinki"),
    Timestamp("2016-10-30 03:00:00+0200", tz="Europe/Helsinki"),
]
result = DatetimeIndex(ts)
expected = DatetimeIndex([ts[0].to_pydatetime(), ts[1].to_pydatetime()])
tm.assert_index_equal(result, expected)
