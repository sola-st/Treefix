# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
# GH 18271
s = Series(np.arange(2**24 + 1))
result = s.rank(pct=True).max()
assert result == 1
