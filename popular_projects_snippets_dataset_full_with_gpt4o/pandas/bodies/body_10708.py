# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_missing.py
# GH 9304
df = DataFrame({"a": [1, 1, np.nan], "b": [2, 3, 4], "c": [5, 6, 7]})
g = df.groupby(["a", "b"])
result = g.indices
expected = {(1.0, 2): np.array([0]), (1.0, 3): np.array([1])}
assert result == expected
