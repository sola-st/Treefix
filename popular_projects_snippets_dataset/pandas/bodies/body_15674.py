# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# see GH-10633, GH-24014
s = Series([0, 1, np.nan, 3])
msg = "You must specify the order of the spline or polynomial"
with pytest.raises(ValueError, match=msg):
    s.interpolate(method=method)
