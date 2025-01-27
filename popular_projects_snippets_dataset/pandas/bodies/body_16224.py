# Extracted from ./data/repos/pandas/pandas/tests/series/test_missing.py
# GH#19700
idx = Index([0, 1])
assert idx.hasnans is False
assert "hasnans" in idx._cache
ser = idx.to_series()
assert ser.hasnans is False
assert not hasattr(ser, "_cache")
ser.iloc[-1] = np.nan
assert ser.hasnans is True
assert Series.hasnans.__doc__ == Index.hasnans.__doc__
