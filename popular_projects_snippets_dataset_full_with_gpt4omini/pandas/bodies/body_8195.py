# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
dr = date_range("2012-06-02", periods=10, tz=tzstr, name="foo")
dr2 = DatetimeIndex(list(dr), name="foo", freq="D")
tm.assert_index_equal(dr, dr2)
