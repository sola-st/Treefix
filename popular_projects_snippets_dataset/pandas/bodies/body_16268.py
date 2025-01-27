# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 17088

s = Series(Index([0, 2, 4]), dtype=dtype)
assert s.dtype == dtype
