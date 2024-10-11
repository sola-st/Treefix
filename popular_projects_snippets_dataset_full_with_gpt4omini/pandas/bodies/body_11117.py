# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 6265
result = df.groupby("A")["C"]
assert result.count().name == "C"
assert result.mean().name == "C"

testFunc = lambda x: np.sum(x) * 2
assert result.agg(testFunc).name == "C"
