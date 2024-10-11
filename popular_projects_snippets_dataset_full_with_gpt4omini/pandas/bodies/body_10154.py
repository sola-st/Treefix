# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 14013
df = DataFrame({"A": ["foo"] * 3 + ["bar"] * 3, "B": [1] * 6})
g = df.groupby("A")

mi = MultiIndex.from_tuples(
    [("bar", 3), ("bar", 4), ("bar", 5), ("foo", 0), ("foo", 1), ("foo", 2)]
)

mi.names = ["A", None]
# Grouped column should not be a part of the output
expected = DataFrame([np.nan, 2.0, 2.0] * 2, columns=["B"], index=mi)

result = g.rolling(window=2).sum()
tm.assert_frame_equal(result, expected)

# Call an arbitrary function on the groupby
g.sum()

# Make sure nothing has been mutated
result = g.rolling(window=2).sum()
tm.assert_frame_equal(result, expected)
