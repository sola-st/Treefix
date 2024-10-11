# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# if we passed a NaT it remains
s = Series([datetime(2010, 1, 1), datetime(2, 1, 1), NaT])
assert s.dtype == "object"
assert s[2] is NaT
assert "NaT" in str(s)
