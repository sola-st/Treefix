# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 18271
values = np.arange(2**24 + 1)
result = algos.rank(values, pct=True).max()
assert result == 1

values = np.arange(2**25 + 2).reshape(2**24 + 1, 2)
result = algos.rank(values, pct=True).max()
assert result == 1
