# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# Check numpy masked arrays with hard masks -- from GH24574
data = ma.masked_all((3,), dtype=float).harden_mask()
result = Series(data)
expected = Series([np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)
