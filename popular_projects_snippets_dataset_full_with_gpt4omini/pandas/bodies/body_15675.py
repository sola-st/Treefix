# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([0, 1, np.nan, 3])
msg = "order needs to be specified and greater than 0"
with pytest.raises(ValueError, match=msg):
    s.interpolate(method="spline", order=order)
