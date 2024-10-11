# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH 26989
# DataFrame.at getter works with Index of tuples
df = DataFrame({"a": [1, 2]}, index=[(1, 2), (3, 4)])
assert df.index.nlevels == 1
assert df.at[(1, 2), "a"] == 1

# Series.at getter works with Index of tuples
series = df["a"]
assert series.index.nlevels == 1
assert series.at[(1, 2)] == 1
