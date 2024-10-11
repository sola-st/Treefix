# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# When method='time' is used on a non-TimeSeries that contains a null
# value, a ValueError should be raised.
non_ts = Series([0, 1, 2, np.NaN])
msg = "time-weighted interpolation only works on Series.* with a DatetimeIndex"
with pytest.raises(ValueError, match=msg):
    non_ts.interpolate(method="time")
