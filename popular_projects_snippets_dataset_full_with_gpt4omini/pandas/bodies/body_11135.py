# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH #36842: Grouping over two group keys shouldn't raise an error
df = DataFrame({"a": [np.nan, np.nan], "b": [np.nan, np.nan], "c": [1, 2]})
result = df.groupby(["a", "b"]).indices
assert result == {}
