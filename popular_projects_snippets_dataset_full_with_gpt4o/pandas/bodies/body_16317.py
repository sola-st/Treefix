# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# non-convertible
s = Series([1479596223000, -1479590, NaT])
assert s.dtype == "object"
assert s[2] is NaT
assert "NaT" in str(s)
