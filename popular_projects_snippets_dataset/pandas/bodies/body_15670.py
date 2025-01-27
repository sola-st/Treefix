# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, np.nan, 3], index=[0, 2, 1])
msg = "krogh interpolation requires that the index be monotonic"
with pytest.raises(ValueError, match=msg):
    s.interpolate(method="krogh")
