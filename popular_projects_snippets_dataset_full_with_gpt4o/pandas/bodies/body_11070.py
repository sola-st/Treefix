# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = tm.makeTimeDataFrame()
grouped = df.groupby([lambda x: x.year, lambda x: x.month, lambda x: x.day])
assert len(grouped) == len(df)

grouped = df.groupby([lambda x: x.year, lambda x: x.month])
expected = len({(x.year, x.month) for x in df.index})
assert len(grouped) == expected

# issue 11016
df = DataFrame({"a": [np.nan] * 3, "b": [1, 2, 3]})
assert len(df.groupby("a")) == 0
assert len(df.groupby("b")) == 3
assert len(df.groupby(["a", "b"])) == 3
