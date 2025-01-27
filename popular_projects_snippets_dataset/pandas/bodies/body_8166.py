# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# Regression test for:
# https://github.com/pandas-dev/pandas/issues/13306

# sorted case US/Eastern -> UTC
ts = ["2008-05-12 09:50:00", "2008-12-12 09:50:35", "2009-05-12 09:50:32"]
tt = DatetimeIndex(ts).tz_localize("US/Eastern")
ut = tt.tz_convert("UTC")
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)

# sorted case UTC -> US/Eastern
ts = ["2008-05-12 13:50:00", "2008-12-12 14:50:35", "2009-05-12 13:50:32"]
tt = DatetimeIndex(ts).tz_localize("UTC")
ut = tt.tz_convert("US/Eastern")
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)

# unsorted case US/Eastern -> UTC
ts = ["2008-05-12 09:50:00", "2008-12-12 09:50:35", "2008-05-12 09:50:32"]
tt = DatetimeIndex(ts).tz_localize("US/Eastern")
ut = tt.tz_convert("UTC")
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)

# unsorted case UTC -> US/Eastern
ts = ["2008-05-12 13:50:00", "2008-12-12 14:50:35", "2008-05-12 13:50:32"]
tt = DatetimeIndex(ts).tz_localize("UTC")
ut = tt.tz_convert("US/Eastern")
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
