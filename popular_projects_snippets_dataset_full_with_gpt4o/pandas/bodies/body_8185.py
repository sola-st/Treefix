# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# November 6, 2011, fall back, repeat 2 AM hour

# Pass in flags to determine right dst transition
dr = date_range(
    datetime(2011, 11, 6, 0), periods=5, freq=pd.offsets.Hour(), tz=tz
)
times = [
    "11/06/2011 00:00",
    "11/06/2011 01:00",
    "11/06/2011 01:00",
    "11/06/2011 02:00",
    "11/06/2011 03:00",
]

# Test tz_localize
di = DatetimeIndex(times)
is_dst = [1, 1, 0, 0, 0]
localized = di.tz_localize(tz, ambiguous=is_dst)
expected = dr._with_freq(None)
tm.assert_index_equal(expected, localized)
tm.assert_index_equal(expected, DatetimeIndex(times, tz=tz, ambiguous=is_dst))

localized = di.tz_localize(tz, ambiguous=np.array(is_dst))
tm.assert_index_equal(dr, localized)

localized = di.tz_localize(tz, ambiguous=np.array(is_dst).astype("bool"))
tm.assert_index_equal(dr, localized)

# Test constructor
localized = DatetimeIndex(times, tz=tz, ambiguous=is_dst)
tm.assert_index_equal(dr, localized)

# Test duplicate times where inferring the dst fails
times += times
di = DatetimeIndex(times)

# When the sizes are incompatible, make sure error is raised
msg = "Length of ambiguous bool-array must be the same size as vals"
with pytest.raises(Exception, match=msg):
    di.tz_localize(tz, ambiguous=is_dst)

# When sizes are compatible and there are repeats ('infer' won't work)
is_dst = np.hstack((is_dst, is_dst))
localized = di.tz_localize(tz, ambiguous=is_dst)
dr = dr.append(dr)
tm.assert_index_equal(dr, localized)

# When there is no dst transition, nothing special happens
dr = date_range(datetime(2011, 6, 1, 0), periods=10, freq=pd.offsets.Hour())
is_dst = np.array([1] * 10)
localized = dr.tz_localize(tz)
localized_is_dst = dr.tz_localize(tz, ambiguous=is_dst)
tm.assert_index_equal(localized, localized_is_dst)
