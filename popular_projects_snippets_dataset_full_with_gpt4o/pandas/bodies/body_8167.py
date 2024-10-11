# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# Regression test for GH#13306

# sorted case US/Eastern -> UTC
ts = [
    Timestamp("2008-05-12 09:50:00", tz=tz),
    Timestamp("2008-12-12 09:50:35", tz=tz),
    Timestamp("2009-05-12 09:50:32", tz=tz),
]
tt = DatetimeIndex(ts)
ut = tt.tz_convert("UTC")
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)

# sorted case UTC -> US/Eastern
ts = [
    Timestamp("2008-05-12 13:50:00", tz="UTC"),
    Timestamp("2008-12-12 14:50:35", tz="UTC"),
    Timestamp("2009-05-12 13:50:32", tz="UTC"),
]
tt = DatetimeIndex(ts)
ut = tt.tz_convert("US/Eastern")
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)

# unsorted case US/Eastern -> UTC
ts = [
    Timestamp("2008-05-12 09:50:00", tz=tz),
    Timestamp("2008-12-12 09:50:35", tz=tz),
    Timestamp("2008-05-12 09:50:32", tz=tz),
]
tt = DatetimeIndex(ts)
ut = tt.tz_convert("UTC")
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)

# unsorted case UTC -> US/Eastern
ts = [
    Timestamp("2008-05-12 13:50:00", tz="UTC"),
    Timestamp("2008-12-12 14:50:35", tz="UTC"),
    Timestamp("2008-05-12 13:50:32", tz="UTC"),
]
tt = DatetimeIndex(ts)
ut = tt.tz_convert("US/Eastern")
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
