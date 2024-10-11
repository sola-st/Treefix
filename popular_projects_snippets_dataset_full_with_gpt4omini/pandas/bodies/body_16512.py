# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 3820
a = np.array(["foo", "foo", "foo", "bar", "bar", "foo", "foo"], dtype=object)
b = np.array(["one", "one", "two", "one", "two", "two", "two"], dtype=object)
c = np.array(
    ["dull", "dull", "dull", "dull", "dull", "shiny", "shiny"], dtype=object
)
res = crosstab(a, [b, c], rownames=["a"], colnames=["b", "c"], dropna=False)
m = MultiIndex.from_tuples(
    [("one", "dull"), ("one", "shiny"), ("two", "dull"), ("two", "shiny")],
    names=["b", "c"],
)
tm.assert_index_equal(res.columns, m)
