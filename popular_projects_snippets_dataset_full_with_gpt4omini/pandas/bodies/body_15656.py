# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 3, np.nan, 12, np.nan, 25])

msg = f"method must be one of.* Got '{invalid_method}' instead"
with pytest.raises(ValueError, match=msg):
    s.interpolate(method=invalid_method)

# When an invalid method and invalid limit (such as -1) are
# provided, the error message reflects the invalid method.
with pytest.raises(ValueError, match=msg):
    s.interpolate(method=invalid_method, limit=-1)
