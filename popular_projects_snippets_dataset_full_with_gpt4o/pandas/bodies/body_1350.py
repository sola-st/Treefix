# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH24919
s = Series([1, 2])
result = s.iloc[np.array(0)]
assert result == 1
