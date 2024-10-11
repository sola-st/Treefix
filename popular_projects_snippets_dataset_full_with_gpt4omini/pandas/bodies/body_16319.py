# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# if we passed a nan it remains
s = Series([datetime(2010, 1, 1), datetime(2, 1, 1), np.nan])
assert s.dtype == "object"
assert s[2] is np.nan
assert "NaN" in str(s)
