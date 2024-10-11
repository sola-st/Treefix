# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH-23077
cat = pd.Categorical(["a", "a", "b", "c"])
df = DataFrame({"A": cat, "B": cat})
result = df.stack()
index = MultiIndex.from_product([[0, 1, 2, 3], ["A", "B"]])
expected = Series(
    pd.Categorical(["a", "a", "a", "a", "b", "b", "c", "c"]), index=index
)
tm.assert_series_equal(result, expected)
