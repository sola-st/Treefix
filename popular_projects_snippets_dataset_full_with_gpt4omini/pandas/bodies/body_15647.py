# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 3, np.nan, np.nan, np.nan, 11])
msg = (
    "time-weighted interpolation only works on Series or DataFrames "
    "with a DatetimeIndex"
)
with pytest.raises(ValueError, match=msg):
    s.interpolate(method="time")
