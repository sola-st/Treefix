# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 3, np.nan, np.nan, np.nan, 11])

msg = (
    r"Invalid limit_direction: expecting one of \['forward', "
    r"'backward', 'both'\], got 'abc'"
)
with pytest.raises(ValueError, match=msg):
    s.interpolate(method="linear", limit=2, limit_direction="abc")

# raises an error even if no limit is specified.
with pytest.raises(ValueError, match=msg):
    s.interpolate(method="linear", limit_direction="abc")
