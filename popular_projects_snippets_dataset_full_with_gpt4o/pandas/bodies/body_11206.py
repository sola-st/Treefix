# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 42795
df = DataFrame({"a": [1, 2], "b": [np.nan, 5], "c": [np.nan, 2]}, index=["x", "y"])
result = [key for key, _ in df.groupby(["a"])]
expected = [(1,), (2,)]
assert result == expected
