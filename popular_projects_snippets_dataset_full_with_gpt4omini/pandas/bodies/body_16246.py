# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# pre-2.0 these would be silently ignored and come back with object dtype
vals = ["aa"]
msg = "^Unknown datetime string format, unable to parse: aa, at position 0$"
with pytest.raises(ValueError, match=msg):
    Series(vals, dtype="datetime64[ns]")

with pytest.raises(ValueError, match=msg):
    Series(np.array(vals, dtype=object), dtype="datetime64[ns]")
