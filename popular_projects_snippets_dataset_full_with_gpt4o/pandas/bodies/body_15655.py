# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH 9217: make sure limit is an integer.
s = Series([1, 2, np.nan, 4])
method, kwargs = nontemporal_method
limit = 2.0
with pytest.raises(ValueError, match="Limit must be an integer"):
    s.interpolate(limit=limit, method=method, **kwargs)
