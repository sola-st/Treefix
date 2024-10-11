# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# Test small Series.
s = Series([0, 1, 2])

s.name = "test"
assert "Name: test" in repr(s)

s.name = None
assert "Name:" not in repr(s)
