# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH 9217: make sure limit is greater than zero.
s = Series([1, 2, np.nan, 4])
method, kwargs = nontemporal_method
with pytest.raises(ValueError, match="Limit must be greater than 0"):
    s.interpolate(limit=limit, method=method, **kwargs)
