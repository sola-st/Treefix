# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_searchsorted.py
# GH#49620
ser = Series([1, 2, 3, 4, 5])
vals = pd.DataFrame([[1, 2], [3, 4]])
msg = "Value must be 1-D array-like or scalar, DataFrame is not supported"
with pytest.raises(ValueError, match=msg):
    ser.searchsorted(vals)
