# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
"""Test different DatetimeIndex constructions with timezone
        Follow-up of GH#4229
        """
arr = ["11/10/2005 08:00:00", "11/10/2005 09:00:00"]

idx1 = to_datetime(arr).tz_localize(tzstr)
idx2 = date_range(start="2005-11-10 08:00:00", freq="H", periods=2, tz=tzstr)
idx2 = idx2._with_freq(None)  # the others all have freq=None
idx3 = DatetimeIndex(arr, tz=tzstr)
idx4 = DatetimeIndex(np.array(arr), tz=tzstr)

for other in [idx2, idx3, idx4]:
    tm.assert_index_equal(idx1, other)
