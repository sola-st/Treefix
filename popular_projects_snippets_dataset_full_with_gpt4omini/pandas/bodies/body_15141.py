# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# Test big Series (diff code path).
s = Series(range(1000))

s.name = "test"
assert "Name: test" in repr(s)

s.name = None
assert "Name:" not in repr(s)
